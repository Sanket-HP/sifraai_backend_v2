
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import upload, eda, quality, anonymize, automl, compare, explain, anomaly, forecast, nlp_query, report, codegen, pipeline, plugins, datasource, share, templates, chat, bi_export, versioning, public, models, correlation, trend, notebook

app = FastAPI(title="Sifra AI Backend v2", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
for router in [
    upload.router, eda.router, quality.router, anonymize.router, automl.router, compare.router,
    explain.router, anomaly.router, forecast.router, nlp_query.router, report.router, codegen.router,
    pipeline.router, plugins.router, datasource.router, share.router, templates.router, chat.router,
    bi_export.router, versioning.router, public.router, models.router, correlation.router, trend.router, notebook.router
]:
    app.include_router(router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok", "service": "sifra-ai-backend-v2"}
