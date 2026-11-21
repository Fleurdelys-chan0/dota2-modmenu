import platform
import sys

import psutil


def log_environment() -> None:
    print(f"python      : {sys.version.split()[0]}")
    print(f"platform    : {platform.platform()}")
    print(f"arch        : {platform.machine()}")
    for p in psutil.process_iter(["name", "pid"]):
        if p.info["name"] and "dota2" in p.info["name"].lower():
            print(f"dota2 found : pid={p.info['pid']}")


def run_diagnostics() -> None:
    log_environment()
</｜｜DSML｜｜ parameter>