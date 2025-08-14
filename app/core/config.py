
import os
from pathlib import Path

DATA_DIR = Path(os.environ.get("SIFRA_DATA_DIR", Path(__file__).resolve().parents[1] / "data"))
REPORT_DIR = Path(os.environ.get("SIFRA_REPORT_DIR", Path(__file__).resolve().parents[1] / "static" ) ) / "reports"
PLUGIN_DIR = Path(os.environ.get("SIFRA_PLUGIN_DIR", Path(__file__).resolve().parents[1] / "plugins"))
REGISTRY_PATH = Path(os.environ.get("SIFRA_REGISTRY_PATH", DATA_DIR / "registry.json"))

for d in [DATA_DIR, REPORT_DIR, PLUGIN_DIR]:
    d.mkdir(parents=True, exist_ok=True)
