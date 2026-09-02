# Architecture

CyberFlix is split into narrowly scoped CSS modules. This keeps regressions isolated and makes Jellyfin selector changes easier to diagnose.

## Module order

1. `00-tokens.css` — design tokens only.
2. `05-foundation.css` — global resets and common primitives.
3. `10-background.css` — page atmosphere.
4. `20-header.css` — top navigation.
5. `30-home.css` — home rows and hierarchy.
6. `40-cards.css` — card geometry and artwork-safe presentation.
7. `45-overlay.css` — hover/focus actions and gradients.
8. `50-details.css` — media detail pages.
9. `55-library.css` — library grids and filters.
10. `60-ui.css` — drawers, dialogs and controls.
11. `65-search.css` — search presentation.
12. `70-login.css` — authentication and user selection.
13. `75-player.css` — player OSD.
14. `80-settings.css` — settings and dashboard.
15. `85-feedback.css` — progress, loading and notifications.
16. `90-responsive.css` — device breakpoints.
17. `95-accessibility.css` — focus and reduced-motion behavior.

## Artwork safety rule

Never set `background`, `background-image`, or a replacement image on `.cardImageContainer`. Jellyfin uses that element for media artwork.
