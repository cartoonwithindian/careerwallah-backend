from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, opportunities, students, roadmaps, projects, feedback, professionals, counsellors, bookings, language, recommendations
from app.db.session import engine
from app.models import Base

app = FastAPI(title="Careerwallah - Rural Opportunity Bridge API", version="0.1.0")
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.api_v1_prefix)
app.include_router(opportunities.router, prefix=settings.api_v1_prefix)
app.include_router(students.router, prefix=settings.api_v1_prefix)
app.include_router(roadmaps.router, prefix=settings.api_v1_prefix)
app.include_router(projects.router, prefix=settings.api_v1_prefix)
app.include_router(feedback.router, prefix=settings.api_v1_prefix)
app.include_router(professionals.router, prefix=settings.api_v1_prefix)
app.include_router(counsellors.router, prefix=settings.api_v1_prefix)
app.include_router(bookings.router, prefix=settings.api_v1_prefix)
app.include_router(recommendations.router, prefix=settings.api_v1_prefix)
app.include_router(language.router, prefix=settings.api_v1_prefix)


@app.get("/")
def root():
    return {"message": "Careerwallah API", "docs": "/docs"}
