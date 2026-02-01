#!/usr/bin/env python
"""Sync this skill from the Orchard-Core-Agent-Skills repo."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

DEFAULT_REPO_URL = "https://github.com/Lombiq/Orchard-Core-Agent-Skills"
DEFAULT_REF = "main"
DEFAULT_SKILL_PATH = "skills/orchard-core-theming"


def run(cmd: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def clone_repo(repo_url: str, ref: str, dest: Path) -> None:
    run(["git", "clone", "--depth", "1", "--branch", ref, repo_url, str(dest)])


def build_source_sets(src_root: Path) -> tuple[set[Path], set[Path]]:
    src_files: set[Path] = set()
    src_dirs: set[Path] = set()
    for dirpath, dirnames, filenames in os.walk(src_root):
        rel_dir = Path(dirpath).relative_to(src_root)
        if rel_dir != Path("."):
            src_dirs.add(rel_dir)
        for dirname in dirnames:
            src_dirs.add(rel_dir / dirname)
        for filename in filenames:
            src_files.add(rel_dir / filename)
    return src_files, src_dirs


def is_excluded(rel_path: Path, excluded: set[Path]) -> bool:
    if rel_path in excluded:
        return True
    return "__pycache__" in rel_path.parts


def remove_stale(
    dest_root: Path,
    src_files: set[Path],
    src_dirs: set[Path],
    excluded: set[Path],
) -> None:
    for dirpath, dirnames, filenames in os.walk(dest_root, topdown=False):
        rel_dir = Path(dirpath).relative_to(dest_root)

        for filename in filenames:
            rel_path = rel_dir / filename
            if is_excluded(rel_path, excluded):
                continue
            if rel_path in src_dirs or rel_path not in src_files:
                (dest_root / rel_path).unlink(missing_ok=True)

        for dirname in dirnames:
            rel_path = rel_dir / dirname
            if is_excluded(rel_path, excluded):
                continue
            if rel_path in src_files or rel_path not in src_dirs:
                shutil.rmtree(dest_root / rel_path, ignore_errors=True)


def copy_updates(
    src_root: Path,
    dest_root: Path,
    src_files: set[Path],
    excluded: set[Path],
) -> None:
    for rel_path in sorted(src_files):
        if is_excluded(rel_path, excluded):
            continue
        dest_path = dest_root / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_root / rel_path, dest_path)


def sync_skill_folder(src_root: Path, dest_root: Path, excluded: set[Path]) -> None:
    src_files, src_dirs = build_source_sets(src_root)
    dest_root.mkdir(parents=True, exist_ok=True)
    remove_stale(dest_root, src_files, src_dirs, excluded)
    copy_updates(src_root, dest_root, src_files, excluded)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL)
    parser.add_argument("--ref", default=DEFAULT_REF)
    parser.add_argument(
        "--local-repo",
        default=None,
        help="Use an existing local Orchard-Core-Agent-Skills clone (no checkout).",
    )
    parser.add_argument("--skill-path", default=DEFAULT_SKILL_PATH)
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    excluded: set[Path] = set()
    current_script = Path(__file__).resolve().relative_to(skill_root)
    excluded.add(current_script)

    if args.local_repo:
        repo_dir = Path(args.local_repo).resolve()
        if not repo_dir.exists():
            raise SystemExit(f"Local repo not found: {repo_dir}")
        cleanup = None
    else:
        temp_dir = tempfile.TemporaryDirectory()
        repo_dir = Path(temp_dir.name)
        clone_repo(args.repo_url, args.ref, repo_dir)
        cleanup = temp_dir

    try:
        skill_src = repo_dir / args.skill_path
        if not skill_src.exists():
            raise SystemExit(f"Skill path not found: {skill_src}")
        sync_skill_folder(skill_src, skill_root, excluded)
    finally:
        if cleanup is not None:
            cleanup.cleanup()


if __name__ == "__main__":
    main()
