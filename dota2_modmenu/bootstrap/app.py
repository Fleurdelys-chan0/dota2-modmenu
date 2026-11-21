import logging
import signal
import sys

from dota2_modmenu.bootstrap.config_loader import load_config
from dota2_modmenu.bootstrap.diagnostics import log_environment
from dota2_modmenu.injector.process_attach import DotaProcessWatcher
from dota2_modmenu.signatures.offset_resolver import OffsetResolver
from dota2_modmenu.overlay.renderer import OverlayRenderer
from dota2_modmenu.skins.catalog import SkinCatalog
from dota2_modmenu.ipc.bridge_server import BridgeServer

log = logging.getLogger("d2mm.app")


class ModMenuApp:
    """Top-level application shell. Wires watcher -> services -> IPC bridge."""

    def __init__(self, config_path: str | None = None, overlay: bool = True) -> None:
        self.config = load_config(config_path)
        self.overlay_enabled = overlay
        self._shutdown = False

    def run(self) -> int:
        log_environment()
        logging.basicConfig(level=self.config.app.log_level.upper())

        resolver = OffsetResolver(self.config.signatures.signature_dir)
        resolver.load()

        catalog = SkinCatalog(self.config.skins.catalog_dir)
        catalog.load()

        watcher = DotaProcessWatcher(self.config.injector)
        watcher.on_attach(lambda proc: log.info("attached to pid=%s", proc.pid))
        watcher.on_detach(lambda: log.warning("dota2 process lost"))

        bridge = BridgeServer(
            host="127.0.0.1",
            port=7411,
            context={"resolver": resolver, "catalog": catalog, "watcher": watcher},
        )
        bridge.start()

        if self.overlay_enabled:
            renderer = OverlayRenderer(self.config.overlay)
            renderer.start()

        signal.signal(signal.SIGINT, self._on_sigint)
        watcher.run_forever()
        return 0

    def _on_sigint(self, *_args) -> None:
        log.info("shutdown requested")
        self._shutdown = True