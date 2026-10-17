from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter(prefix="/language", tags=["language"])


@router.post("/explain-recommendations")
def explain_recommendations(payload: Dict[str, Any]):
    return {
        "explanation": "AI-generated explanation (demo mode - not using Sarvam API)",
        "language": payload.get("language", "en"),
        "is_ai_generated": True,
    }


@router.post("/translate")
def translate(payload: Dict[str, Any]):
    return {
        "translated_text": payload.get("text", ""),
        "source_language": payload.get("source_language", "en"),
        "target_language": payload.get("target_language", "hi"),
        "is_ai_generated": True,
    }


@router.post("/text-to-speech")
def text_to_speech(payload: Dict[str, Any]):
    return {
        "audio_url": None,
        "message": "Text-to-speech not configured (no Sarvam API key)",
        "is_ai_generated": False,
    }
