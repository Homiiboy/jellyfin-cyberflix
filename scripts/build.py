from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

ORDER = [
    "00-tokens.css",
    "05-foundation.css",
    "10-background.css",
    "20-header.css",
    "30-home.css",
    "40-cards.css",
    "45-overlay.css",
    "50-details.css",
    "55-library.css",
    "60-ui.css",
    "65-search.css",
    "70-login.css",
    "75-player.css",
    "80-settings.css",
    "85-feedback.css",
    "90-responsive.css",
    "95-accessibility.css",
]

parts = [(ROOT / "src" / name).read_text(encoding="utf-8").rstrip() for name in ORDER]
(ROOT / "dist").mkdir(exist_ok=True)

bundle_header = f"/*! CyberFlix {VERSION} for Jellyfin Web — standalone bundle */\n\n"
(ROOT / "dist" / "bundle.css").write_text(
    bundle_header + "\n\n".join(parts) + "\n",
    encoding="utf-8",
)

loader = [
    "/*!",
    f" * CyberFlix {VERSION} for Jellyfin Web",
    " * Runtime module loader",
    " */",
]
loader += [f'@import url("../src/{name}?v={VERSION}");' for name in ORDER]
(ROOT / "dist" / "theme.css").write_text("\n".join(loader) + "\n", encoding="utf-8")

print(f"Built CyberFlix {VERSION}: dist/theme.css + dist/bundle.css")
