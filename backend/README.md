# Careerwallah - Rural Opportunity Bridge Backend

FastAPI backend for Rural Opportunity Bridge (AI-assisted career discovery platform).

## Quick Start

1. Create virtualenv (optional)
2. Install deps: `pip install -r requirements.txt`
3. Configure: `cp .env.example .env`
4. Seed data: `cd backend && python ../scripts/seed_opportunities.py`
5. Run: `cd backend && uvicorn app.main:app --reload`

## API Docs
- Swagger: http://localhost:8000/docs
- Health: http://localhost:8000/api/v1/health

## Testing
- `cd backend && python -m pytest tests/`

## Dataset
Sample dataset in `backend/app/data/rural_opportunity_bridge_dataset.json`
