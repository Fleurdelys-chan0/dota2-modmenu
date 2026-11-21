# Contributing to dota2-modmenu

Thanks for wanting to help out. This is a hobbyist DOTA2 modding project — PRs for new
hero skin mappings, offset signatures, and overlay rendering tweaks are especially welcome.

## Ground rules

- Do **not** commit live Steam credentials, session tokens, or anything that touches
  the VAC-secured client in a way that could be flagged as account-banned material.
- Offsets and signatures go in `signatures/` as JSON. Bump the `build` field whenever
  a DOTA2 patch lands.
- Keep the overlay renderer frame budget under 4ms. `scripts/profile_overlay.py` helps.
- Python 3.11+ is required. Run `python -m pytest tests/` before opening a PR.

## Adding a new skin definition

1. Drop a JSON file into `skins/catalog/heroes/<hero_slug>.json`
2. Add the item def index to `skins/catalog/index_map.json`
3. Open a PR titled `skins: add <hero name>` — screenshots welcome but not required.

## Reporting bugs

Use the issue template. Include your Windows build, Python version, and the output of
`python -m dota2_modmenu --diagnose`.