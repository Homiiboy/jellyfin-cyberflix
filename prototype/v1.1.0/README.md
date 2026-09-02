# CyberFlix for Jellyfin

Netflix-inspired Jellyfin Web theme with cyberpunk cyan, purple and magenta accents.

## Install

After publishing this repository to GitHub, open:

**Jellyfin Dashboard → General → Custom CSS**

and paste only:

```css
@import url("https://cdn.jsdelivr.net/gh/Homiiboy/jellyfin-cyberflix@main/dist/theme.css");
```

Then save and hard-refresh Jellyfin with `Ctrl + F5`.

## Stable release URL

For a tagged release, use:

```css
@import url("https://cdn.jsdelivr.net/gh/Homiiboy/jellyfin-cyberflix@1.0.0/dist/theme.css");
```

## Development

Edit the files in `src/`, then rebuild:

```bash
python scripts/build.py
```

Jellyfin loads:

```text
dist/theme.css
```

## Project structure

```text
jellyfin-cyberflix/
├─ dist/
│  └─ theme.css
├─ src/
│  ├─ 00-tokens.css
│  ├─ 10-background.css
│  ├─ 20-header.css
│  ├─ 30-home.css
│  ├─ 40-cards.css
│  ├─ 50-details.css
│  ├─ 60-ui.css
│  └─ 90-responsive.css
├─ scripts/
│  └─ build.py
├─ theme.css
├─ LICENSE
└─ README.md
```

## Notes

- Designed for Jellyfin Web.
- Native apps may ignore some custom CSS.
- Card artwork stays under Jellyfin's control; the theme does not replace card `background-image` values.
