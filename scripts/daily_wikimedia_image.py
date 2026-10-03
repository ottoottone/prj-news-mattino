#!/usr/bin/env python3
"""Fetch a Wikimedia Commons image and render a Neon Commons dot-field asset."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

API = "https://commons.wikimedia.org/w/api.php"
UA = "GermaniaInBreve/1.0 (editorial image fetcher; contact site maintainer)"
PALETTE = ((255, 79, 135), (124, 77, 255), (255, 222, 2))


def fetch_json(params: dict) -> dict:
    url = API + "?" + urlencode(params)
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value[:70] or "wikimedia-subject"


def choose_file(query: str) -> dict:
    data = fetch_json({
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,
        "gsrlimit": 15,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size|mime",
        "iiurlwidth": 1600,
        "format": "json",
        "formatversion": 2,
    })
    pages = data.get("query", {}).get("pages", [])
    candidates = []
    for page in pages:
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata") or {}
        mime = info.get("mime", "")
        if not mime.startswith("image/") or not info.get("thumburl"):
            continue
        license_name = (meta.get("LicenseShortName") or {}).get("value", "").strip()
        author = (meta.get("Artist") or {}).get("value", "").strip()
        candidates.append({
            "title": page.get("title", ""),
            "page_url": "https://commons.wikimedia.org/wiki/" + page.get("title", "").replace(" ", "_"),
            "download_url": info["thumburl"],
            "original_url": info.get("descriptionurl", info.get("url", "")),
            "author": re.sub("<[^>]+>", "", author) or "Autore non indicato",
            "license": re.sub("<[^>]+>", "", license_name) or "Licenza indicata nella pagina Wikimedia Commons",
            "width": info.get("width", 0),
            "height": info.get("height", 0),
        })
    if not candidates:
        raise RuntimeError(f"Nessun file immagine Wikimedia Commons trovato per: {query}")
    return candidates[0]


def download(url: str) -> Image.Image:
    req = Request(url, headers={"User-Agent": UA, "Accept": "image/*"})
    with urlopen(req, timeout=60) as response:
        from io import BytesIO
        return Image.open(BytesIO(response.read())).convert("RGB")


def render_dot_field(source: Image.Image, output: Path) -> None:
    canvas = ImageOps.fit(source, (1600, 900), method=Image.Resampling.LANCZOS, centering=(0.5, 0.48))
    gray = ImageOps.grayscale(canvas)
    gray = ImageEnhance.Contrast(gray).enhance(2.0)
    gray = ImageEnhance.Sharpness(gray).enhance(1.8)
    # Deep plum base; dot density follows the source luminance.
    result = Image.new("RGB", canvas.size, (37, 24, 72))
    draw = ImageDraw.Draw(result)
    step = 13
    radius = 4
    for y in range(step // 2, 900, step):
        for x in range(step // 2, 1600, step):
            pixel = gray.getpixel((x, y))
            lum = (float(pixel[0]) if isinstance(pixel, tuple) else float(pixel or 0)) / 255.0
            if lum < 0.12:
                continue
            color = PALETTE[((x // step) + 2 * (y // step)) % len(PALETTE)]
            r = max(1, int(radius * (0.35 + lum * 0.9)))
            draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
    # Subtle dark silhouette layer preserves the focal shape at small sizes.
    silhouette = gray.point(lambda p: 255 if p > 105 else 0).convert("L")
    silhouette = silhouette.filter(ImageFilter.GaussianBlur(1.2))
    overlay = Image.new("RGB", canvas.size, (18, 12, 35))
    result = Image.composite(overlay, result, silhouette.point(lambda p: int(p * 0.22)))
    output.parent.mkdir(parents=True, exist_ok=True)
    result.save(output, format="WEBP", quality=88, method=6)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", required=True)
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--output-dir", default="assets/images/briefing/daily")
    args = parser.parse_args()
    try:
        selected = choose_file(args.subject)
        image = download(selected["download_url"])
        output = Path(args.output_dir) / f"{args.date}-{slug(args.subject)}-dot-field.webp"
        render_dot_field(image, output)
        selected["output_path"] = str(output)
        selected["subject_query"] = args.subject
        print(json.dumps(selected, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc), "subject_query": args.subject}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
