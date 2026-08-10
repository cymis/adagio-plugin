#!/usr/bin/env python3
"""Validate the public Adagio plugin marketplace without third-party packages."""

from __future__ import annotations

import json
import re
import stat
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
APP_ID = re.compile(r"^(?:plugin_)?asdk_app_[0-9A-Za-z]+$")
ALLOWED_SUFFIXES = {".json", ".md", ".svg"}
ALLOWED_EXTENSIONLESS_FILES = {"LICENSE"}


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"Cannot read valid JSON from {path}: {error}") from error
    require(isinstance(value, dict), f"{path} must contain a JSON object")
    return value


def relative_plugin_path(marketplace: dict[str, Any]) -> Path:
    require(marketplace.get("name") == "adagio", "marketplace name must be 'adagio'")
    require(
        marketplace.get("interface", {}).get("displayName") == "Adagio",
        "marketplace display name must be 'Adagio'",
    )
    plugins = marketplace.get("plugins")
    require(isinstance(plugins, list) and len(plugins) == 1, "marketplace must contain one plugin")
    entry = plugins[0]
    require(entry.get("name") == "adagio", "marketplace plugin name must be 'adagio'")
    source = entry.get("source", {})
    require(source.get("source") == "local", "marketplace plugin source must be local")
    source_path = source.get("path")
    require(source_path == "./plugins/adagio", "marketplace source path must be ./plugins/adagio")
    require(
        entry.get("policy")
        == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "marketplace policy must require available installation and authentication on install",
    )
    require(entry.get("category") == "Productivity", "marketplace category must be Productivity")
    return (ROOT / source_path).resolve()


def validate_manifest(plugin_root: Path) -> dict[str, Any]:
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)
    require(plugin_root.name == manifest.get("name") == "adagio", "plugin folder and name must match")
    require(bool(SEMVER.fullmatch(str(manifest.get("version", "")))), "version must be strict semver")
    require(bool(manifest.get("description")), "manifest description is required")
    require(manifest.get("author", {}).get("name") == "Adagio", "manifest author must be Adagio")
    require(
        manifest.get("repository") == "https://github.com/cymis/adagio-plugin",
        "manifest repository must point to the public plugin source",
    )
    require(manifest.get("skills") == "./skills/", "manifest skills path must be ./skills/")
    require(manifest.get("apps") == "./.app.json", "manifest apps path must be ./.app.json")
    require("mcpServers" not in manifest, "do not bundle a second MCP path with the registered app")
    require("hooks" not in manifest, "the public plugin must not contain hooks")

    for field in ("skills", "apps"):
        configured = manifest[field]
        target = (plugin_root / configured).resolve()
        require(target.is_relative_to(plugin_root.resolve()), f"{field} must remain inside plugin root")
        require(target.exists(), f"configured {field} path does not exist: {configured}")

    interface = manifest.get("interface", {})
    for field in ("composerIcon", "logo", "logoDark"):
        configured = interface.get(field)
        require(isinstance(configured, str), f"interface.{field} is required")
        target = (plugin_root / configured).resolve()
        require(target.is_relative_to(plugin_root.resolve()), f"interface.{field} escapes plugin root")
        require(target.is_file(), f"interface.{field} does not exist: {configured}")
    return manifest


def validate_app(plugin_root: Path) -> None:
    app = load_json(plugin_root / ".app.json")
    apps = app.get("apps")
    require(isinstance(apps, dict) and set(apps) == {"adagio"}, ".app.json must map only adagio")
    identifier = apps["adagio"].get("id")
    require(isinstance(identifier, str) and bool(APP_ID.fullmatch(identifier)), "invalid Adagio app ID")
    require("replace" not in identifier.lower(), "app ID still contains a publication placeholder")


def validate_skills(plugin_root: Path) -> None:
    skill_files = sorted((plugin_root / "skills").glob("*/SKILL.md"))
    require(len(skill_files) == 6, "public package must contain the six reviewed Adagio skills")
    names: set[str] = set()
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        require(text.startswith("---\n"), f"{path} must start with YAML front matter")
        match = re.match(r"---\n(.*?)\n---\n", text, flags=re.DOTALL)
        require(match is not None, f"{path} has malformed front matter")
        front_matter = match.group(1)
        name_match = re.search(r"^name:\s*(\S+)\s*$", front_matter, flags=re.MULTILINE)
        description_match = re.search(r"^description:\s*(.+)\s*$", front_matter, flags=re.MULTILINE)
        require(name_match is not None, f"{path} is missing a skill name")
        require(description_match is not None, f"{path} is missing a skill description")
        require(name_match.group(1) not in names, f"duplicate skill name: {name_match.group(1)}")
        names.add(name_match.group(1))


def validate_package_files(plugin_root: Path) -> None:
    for path in plugin_root.rglob("*"):
        require(not path.is_symlink(), f"symlinks are not allowed in the public package: {path}")
        if not path.is_file():
            continue
        require(
            path.suffix in ALLOWED_SUFFIXES or path.name in ALLOWED_EXTENSIONLESS_FILES,
            f"unexpected package file type: {path}",
        )
        require(not (path.stat().st_mode & stat.S_IXUSR), f"executable package file is not allowed: {path}")
        text = path.read_text(encoding="utf-8")
        require("[TODO:" not in text, f"unresolved TODO placeholder in {path}")
        require("replace_after" not in text.lower(), f"publication placeholder in {path}")


def main() -> int:
    try:
        marketplace = load_json(MARKETPLACE_PATH)
        plugin_root = relative_plugin_path(marketplace)
        require(plugin_root.is_dir(), f"plugin root does not exist: {plugin_root}")
        validate_manifest(plugin_root)
        validate_app(plugin_root)
        validate_skills(plugin_root)
        validate_package_files(plugin_root)
    except ValidationError as error:
        print(f"release validation failed: {error}", file=sys.stderr)
        return 1

    print(f"release validation passed: {plugin_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
