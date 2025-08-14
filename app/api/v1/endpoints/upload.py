from fastapi import APIRouter, UploadFile, File, HTTPException
from azure.storage.blob import BlobServiceClient
from app.core.registry import register_dataset, list_datasets
import os

router = APIRouter(prefix="/upload", tags=["Upload (1)"])

# Initialize BlobServiceClient using connection string
connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
container_name = os.environ["AZURE_STORAGE_CONTAINER_NAME"]
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV supported in MVP")
    
    content = await file.read()

    # Upload file to Azure Blob Storage
    blob_client = container_client.get_blob_client(file.filename)
    blob_client.upload_blob(content, overwrite=True)

    # Register dataset (store Azure blob path)
    rec = register_dataset(file.filename, f"azure://{container_name}/{file.filename}", meta={"size": len(content)})
    return {"message": "uploaded", "dataset": rec}

@router.get("/list")
def list_all():
    return list_datasets()
