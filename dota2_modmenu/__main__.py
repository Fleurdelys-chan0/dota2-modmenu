import argparse
import sys

from dota2_modmenu.bootstrap.app import ModMenuApp


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="dota2-modmenu")
    parser.add_argument("--diagnose", action="store_true", help="print environment info and exit")
    parser.add_argument("--config", default=None, help="path to a TOML config file")
    parser.add_argument("--no-overlay", action="store_true", help="disable the overlay")
    args = parser.parse_args(argv)

    if args.diagnose:
        from dota2_modmenu.bootstrap.diagnostics import run_diagnostics
        run_diagnostics()
        return 0

    app = ModMenuApp(config_path=args.config, overlay=not args.no_overlay)
    return app.run()


if __name__ == "__main__":
    sys.exit(main())