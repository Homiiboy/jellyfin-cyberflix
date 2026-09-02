# Development

Development happens on the `develop` branch. `main` remains the stable branch until a tested version is promoted.

## Workflow

1. Change one focused module in `src/`.
2. Run `python scripts/validate.py`.
3. Run `python scripts/build.py`.
4. Test the development import in Jellyfin.
5. Record meaningful changes in `CHANGELOG.md`.
6. Increase `VERSION` and `skin.json` together when releasing a new build.

## Design principles

- Media artwork always wins over decorative CSS.
- Cyberpunk color is an accent, not the entire interface.
- Play is the primary action; secondary actions remain visually quieter.
- Motion must be subtle, fast and optional.
- Desktop, touch and TV focus behavior are all first-class targets.
