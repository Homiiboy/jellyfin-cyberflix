# Releasing

CyberFlix uses `MAJOR.MINOR.PATCH` SemVer without alpha/beta/rc labels.

## Before 1.0.0

- Patch increments (`0.0.1` → `0.0.2`) are normal development iterations.
- Minor increments (`0.0.x` → `0.1.0`) mark meaningful completed milestones.

## From 1.0.0 onward

- PATCH: compatible fixes.
- MINOR: compatible features.
- MAJOR: incompatible redesigns or behavior changes.

## Release checklist

- `VERSION` and `skin.json` match.
- `CHANGELOG.md` contains the release entry.
- Validation succeeds.
- `dist/theme.css` was rebuilt from the exact source modules.
- Desktop and mobile smoke tests pass.
- Poster artwork and playback controls are verified before promotion to `main`.
