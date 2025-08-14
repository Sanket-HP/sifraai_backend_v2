from fastapi import APIRouter, UploadFile, File, HTTPException
from azure.storage.blob import BlobServiceClient
from app.core.registry import register_dataset, list_datasets
import os

router = APIRouter(prefix="/upload", tags=["Upload Files"])

# Azure Blob Storage setup
connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
container_name = "datasets"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Allowed file types
ALLOWED_EXTENSIONS = {".csv", ".json", ".xlsx"}

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Only {', '.join(ALLOWED_EXTENSIONS)} supported")
    
    # Read file content
    content = await file.read()

    # Upload to Azure Blob Storage
    blob_client = container_client.get_blob_client(file.filename)
    blob_client.upload_blob(content, overwrite=True)

    # Build blob URL
    blob_url = f"https://sifraappstorage.blob.core.windows.net/{container_name}/{file.filename}"

    # Register dataset
    rec = register_dataset(file.filename, blob_url, meta={"size": len(content), "extension": ext})

    return {"message": "uploaded", "dataset": rec}

@router.get("/list")
def list_all():
    return list_datasets()
