
import pandas as pd
from pathlib import Path
from app.core.config import DATA_DIR
from app.core.registry import get_dataset

def load_dataset(ds_id):
    rec = get_dataset(ds_id)
    if not rec:
        raise FileNotFoundError(f"Dataset {ds_id} not found")
    path = Path(rec["path"])
    if not path.exists():
        raise FileNotFoundError(f"Dataset file missing at {path}")
    return pd.read_csv(path)
