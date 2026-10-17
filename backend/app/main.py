from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, opportunities

app = FastAPI(title="Careerwallah - Rural Opportunity Bridge API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.api_v1_prefix)
app.include_router(opportunities.router, prefix=settings.api_v1_prefix)


@app.get("/")
def root():
    return {"message": "Careerwallah API", "docs": "/docs"}
