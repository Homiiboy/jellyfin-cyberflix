from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
manifest = json.loads((ROOT / "skin.json").read_text(encoding="utf-8"))

if manifest.get("version") != version:
    raise SystemExit("VERSION and skin.json do not match")

if not re.fullmatch(r"0|[1-9]\d*\.0|0\.\d+\.\d+|[1-9]\d*\.\d+\.\d+", version):
    # Keep validation intentionally conservative but allow the current 0.0.x development line.
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit(f"Invalid SemVer: {version}")

css = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "src").glob("*.css"))
unsafe = re.compile(r"\.cardImageContainer\s*\{[^}]*background(?:-image)?\s*:", re.S)
if unsafe.search(css):
    raise SystemExit("Artwork safety violation: do not set background/background-image on .cardImageContainer")

print(f"CyberFlix {version} validation passed")
