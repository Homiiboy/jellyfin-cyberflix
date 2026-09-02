# CyberFlix

CyberFlix is a full Jellyfin Web skin focused on a cinematic streaming-service UX with subtle cyan, violet and magenta cyberpunk accents.

**Current development version: `0.0.1`**

## Stable installation

The current stable prototype remains on `main`. Your existing Jellyfin import continues to work unchanged:

```css
@import url("https://cdn.jsdelivr.net/gh/Homiiboy/jellyfin-cyberflix/dist/theme.css");
```

## Test the 0.0.1 development skin

Use this only when you intentionally want to test the `develop` branch:

```css
@import url("https://cdn.jsdelivr.net/gh/Homiiboy/jellyfin-cyberflix@develop/dist/theme.css?v=0.0.1");
```

## Development

Source modules live in `src/`. `dist/theme.css` is the file consumed by Jellyfin.

```bash
python scripts/validate.py
python scripts/build.py
```

## Versioning

CyberFlix uses Semantic Versioning beginning at `0.0.1`.

- `0.0.x` — early foundation iterations
- `0.x.0` — larger pre-1.0 milestones
- `1.0.0` — first complete stable skin

## Prototype archive

The original theme prototype is preserved under `prototype/v1.1.0/` and is never loaded by the new skin.
