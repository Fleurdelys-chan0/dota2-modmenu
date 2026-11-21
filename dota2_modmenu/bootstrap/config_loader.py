import os
import tomllib
from pathlib import Path

from dota2_modmenu.models.settings import AppConfig

_DEFAULT_PATH = Path(__file__).resolve().parents[2] / "config" / "default.toml"


def _expand(path: str) -> str:
    return os.path.expandvars(path).replace("%APPDATA%", os.environ.get("APPDATA", ""))


def load_config(user_path: str | None = None) -> AppConfig:
    cfg_path = Path(user_path) if user_path else _DEFAULT_PATH
    with cfg_path.open("rb") as fh:
        raw = tomllib.load(fh)

    # expand env vars in path-bearing fields
    raw["app"]["data_dir"] = _expand(raw["app"]["data_dir"])
    raw["injector"]["dll_path"] = _expand(raw["injector"]["dll_path"])

    return AppConfig.model_validate(raw)