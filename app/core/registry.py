
from .config import REGISTRY_PATH
import json, uuid, datetime

def _load():
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text())
    return {"datasets": {}, "models": {}, "projects": {}}

def _save(obj):
    REGISTRY_PATH.write_text(json.dumps(obj, indent=2, default=str))

def register_dataset(name, path, meta=None):
    db = _load()
    ds_id = str(uuid.uuid4())
    db["datasets"][ds_id] = {
        "id": ds_id, "name": name, "path": str(path), "meta": meta or {},
        "created_at": datetime.datetime.utcnow().isoformat()
    }
    _save(db)
    return db["datasets"][ds_id]

def list_datasets():
    return _load()["datasets"]

def get_dataset(ds_id):
    return _load()["datasets"].get(ds_id)

def set_public(ds_id, is_public=True):
    db = _load()
    if ds_id in db["datasets"]:
        db["datasets"][ds_id]["public"] = bool(is_public)
        _save(db)
        return db["datasets"][ds_id]
    return None

def register_model(name, ds_id, metrics, path=None, meta=None):
    db = _load()
    m_id = str(uuid.uuid4())
    db["models"][m_id] = {"id": m_id, "name": name, "dataset_id": ds_id, "metrics": metrics, "path": path, "meta": meta or {}}
    _save(db)
    return db["models"][m_id]

def list_models():
    return _load()["models"]
