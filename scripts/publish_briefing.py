#!/usr/bin/env python3
"""Deterministic final publication gate for the daily Jekyll briefing."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "ottoottone/prj-news-mattino"
SITE = "https://ottoottone.github.io/prj-news-mattino"


def run(*args: str, check: bool = True, cwd: Path = ROOT, capture: bool = True) -> str:
    p = subprocess.run(args, cwd=cwd, text=True, capture_output=capture)
    if check and p.returncode:
        raise RuntimeError(f"command failed ({p.returncode}): {' '.join(args)}\n{p.stdout}\n{p.stderr}")
    return (p.stdout or "").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", required=True)
    ap.add_argument("--image", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--commit-message", required=True)
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()
    edition = ROOT / args.edition
    image = ROOT / args.image
    if not edition.is_file():
        raise RuntimeError(f"missing edition: {edition}")
    if not image.is_file():
        raise RuntimeError(f"missing image: {image}")
    text = edition.read_text(encoding="utf-8")
    marker = '<figure class="briefing-image briefing-image--daily">'
    summary = text.find('<div class="briefing-summary">')
    figure = text.find(marker)
    article = text.find("<article")
    if summary < 0 or figure < 0 or article < 0 or not (summary < figure < article):
        raise RuntimeError("daily image is not immediately after the briefing summary")
    if args.check_only:
        print(json.dumps({"ok": True, "edition": str(edition), "image": str(image)}))
        return 0
    if (ROOT / "_site").exists():
        stale = Path("/tmp") / f"prj-news-mattino-cron-stale-{int(time.time())}"
        (ROOT / "_site").rename(stale)
    destination = Path("/tmp") / f"prj-news-mattino-cron-build-{int(time.time())}"
    run("bundle", "exec", "jekyll", "build", "--trace", "--destination", str(destination))
    run("git", "diff", "--check")
    run("git", "add", args.edition, args.image, "_data/start_here.yml")
    status = run("git", "status", "--short")
    if not status:
        raise RuntimeError("nothing staged for publication")
    run("git", "commit", "-m", args.commit_message)
    run("git", "push", "origin", "master")
    runs = json.loads(run("gh", "run", "list", "--repo", REPO, "--limit", "5", "--json", "databaseId,headSha,status,conclusion"))
    sha = run("git", "rev-parse", "HEAD")
    current = next((r for r in runs if r.get("headSha") == sha), None)
    if not current:
        raise RuntimeError(f"no Pages workflow found for commit {sha}")
    run("gh", "run", "watch", str(current["databaseId"]), "--repo", REPO, "--exit-status", capture=True)
    code = subprocess.run(["curl", "-L", "--fail", "--silent", "--show-error", "--max-time", "30", args.url], cwd=ROOT, capture_output=True, text=True)
    if code.returncode:
        raise RuntimeError(f"live URL failed: {args.url}\n{code.stderr}")
    final_status = run("git", "status", "--short", "--branch")
    if "\n" in final_status or (final_status and not final_status.startswith("## ")):
        raise RuntimeError(f"repository not clean after publication: {final_status}")
    print(json.dumps({"ok": True, "commit": sha, "url": args.url, "workflow": current["databaseId"]}))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        raise SystemExit(1)
