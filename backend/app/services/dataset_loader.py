import json
from pathlib import Path
from typing import Dict, Any, List


def load_dataset(path: str) -> Dict[str, Any]:
    with open(path) as f:
        return json.load(f)


def normalize_record(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "external_id": item.get("external_id"),
        "title": item.get("title"),
        "category": item.get("category"),
        "provider": item.get("provider"),
        "description": item.get("description"),
        "education_requirements": item.get("education_requirements"),
        "eligibility_criteria": item.get("eligibility_criteria"),
        "required_skills": item.get("required_skills") or [],
        "preferred_skills": item.get("preferred_skills") or [],
        "cost_or_stipend": item.get("cost_or_stipend"),
        "location": item.get("location"),
        "mode": item.get("mode"),
        "device_requirements": item.get("device_requirements"),
        "internet_requirements": item.get("internet_requirements"),
        "official_source_url": item.get("official_source_url"),
        "application_url": item.get("application_url"),
        "application_deadline": item.get("application_deadline"),
        "is_individual_opportunity": bool(item.get("is_individual_opportunity", True)),
        "verification_status": item.get("verification_status"),
        "last_verified": item.get("last_verified"),
    }


def load_and_normalize(path: str) -> Dict[str, Any]:
    data = load_dataset(path)
    normalized = [normalize_record(o) for o in data.get("opportunities", [])]
    return {
        "schema_version": data.get("schema_version"),
        "metadata": data.get("metadata"),
        "opportunities": normalized,
    }
