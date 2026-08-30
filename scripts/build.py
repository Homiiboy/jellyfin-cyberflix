from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = [
    "00-tokens.css",
    "10-background.css",
    "20-header.css",
    "30-home.css",
    "40-cards.css",
    "50-details.css",
    "60-ui.css",
    "90-responsive.css",
]

parts = [(ROOT / "src" / name).read_text(encoding="utf-8").rstrip() for name in ORDER]
header = "/*! CyberFlix for Jellyfin — built from /src */\n\n"
(ROOT / "dist" / "theme.css").write_text(header + "\n\n".join(parts) + "\n", encoding="utf-8")
print("Built dist/theme.css")
