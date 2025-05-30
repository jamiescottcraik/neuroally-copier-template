"""
src.config.settings

Centralized settings/configuration for {{ project_name }}.
- Uses Pydantic for .env loading, validation, and secrets.
- Only fill in values in .env for providers you actually use.
- For production, use a real secret manager (GitHub, AWS, etc).
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    # --- General Settings ---
    ENV: str = "development"
    DEBUG: bool = True
    MAIN_CATEGORY: str = "{{ main_category }}"

    # --- LLM Providers ---
    OPENAI_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    HUGGINGFACE_TOKEN: Optional[str] = None
    COHERE_API_KEY: Optional[str] = None

    # --- Vision APIs ---
    GOOGLE_VISION_API_KEY: Optional[str] = None
    REKOGNITION_ACCESS_KEY: Optional[str] = None
    REKOGNITION_SECRET_KEY: Optional[str] = None
    AZURE_VISION_KEY: Optional[str] = None
    CLARIFAI_API_KEY: Optional[str] = None
    IMAGGA_API_KEY: Optional[str] = None

    # --- Speech APIs ---
    GOOGLE_SPEECH_API_KEY: Optional[str] = None
    AMAZON_TRANSCRIBE_KEY: Optional[str] = None
    AMAZON_POLLY_KEY: Optional[str] = None
    ASSEMBLYAI_API_KEY: Optional[str] = None
    AZURE_SPEECH_KEY: Optional[str] = None

    # --- Generative APIs ---
    DALLE_API_KEY: Optional[str] = None
    STABLE_DIFFUSION_KEY: Optional[str] = None
    DEEPAI_KEY: Optional[str] = None
    IMAGEN_API_KEY: Optional[str] = None
    MAGENTA_API_KEY: Optional[str] = None

    # --- NLP APIs ---
    GOOGLE_NLP_API_KEY: Optional[str] = None
    WATSON_NLU_KEY: Optional[str] = None
    AWS_COMPREHEND_KEY: Optional[str] = None
    AYLIEN_API_KEY: Optional[str] = None

    # --- ML Platforms ---
    VERTEX_AI_KEY: Optional[str] = None
    SAGEMAKER_KEY: Optional[str] = None
    AZURE_ML_KEY: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False
    )


# Singleton instance: import this everywhere
settings = Settings()

# Usage:
# from src.config.settings import settings
# print(settings.OPENAI_API_KEY)
# Note: This file is auto-generated. Do not edit manually.
