
from fastapi import APIRouter
from app.services.utils import load_dataset
from app.core.config import DATA_DIR
import json, uuid

router = APIRouter(prefix="/notebook", tags=["Notebook Export (25)"])

@router.post("/generate")
def generate(ds_id: str):
    nb = {
      "cells": [
        {"cell_type":"code","metadata":{},"source":[
          "import pandas as pd\n",
          "df = pd.read_csv('dataset.csv')\n",
          "df.describe()\n"
        ],"outputs":[],"execution_count":None}
      ],
      "metadata": {"kernelspec":{"name":"python3","display_name":"Python 3"}},
      "nbformat":4,"nbformat_minor":5
    }
    name = f"analysis_{uuid.uuid4().hex}.ipynb"
    path = DATA_DIR / name
    path.write_text(json.dumps(nb, indent=2))
    return {"message":"notebook_ready", "path": str(path)}
