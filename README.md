# CyberFlix

CyberFlix is a full Jellyfin Web skin built around a cinematic streaming-service experience rather than the stock Jellyfin visual language.

**Current development version: `0.0.2`**

## Design direction

CyberFlix combines deep cinema-black surfaces with Stormy Teal navigation accents, Coral/Cherry focus states and rare Gold/Bronze premium highlights. The visual goal is a polished living-room streaming interface with large artwork, restrained chrome and clear content hierarchy.

## Stable installation

The current stable prototype remains on `main`:

```css
@import url("https://cdn.jsdelivr.net/gh/Homiiboy/jellyfin-cyberflix/dist/theme.css");
```

## Test CyberFlix 0.0.2

Use the development branch when testing the new skin:

```css
@import url("https://cdn.jsdelivr.net/gh/Homiiboy/jellyfin-cyberflix@develop/dist/theme.css?v=0.0.2");
```

After changing versions, save Jellyfin Custom CSS and hard-refresh the web client.

## Development

```bash
python scripts/validate.py
python scripts/build.py
```

Source modules live under `src/`; Jellyfin consumes `dist/theme.css`.

## Versioning

- `0.0.x` — rapid early skin iterations
- `0.x.0` — larger pre-1.0 milestones
- `1.0.0` — first complete stable CyberFlix skin

## Prototype archive

The original theme prototype remains preserved under `prototype/v1.1.0/` and is never loaded by the new skin.
