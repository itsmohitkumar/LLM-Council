"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Council members - diverse Groq model identifiers (all currently available)
COUNCIL_MODELS = [
    "llama-3.3-70b-versatile",                          # Most capable production model
    "llama-3.1-8b-instant",                              # Fast, smaller model for different perspective
    "meta-llama/llama-4-maverick-17b-128e-instruct",     # Latest Llama 4 preview, mixture of experts
    "qwen/qwen3-32b",                                    # Qwen model, different architecture
]

# Chairman model - synthesizes final response (using most versatile model)
CHAIRMAN_MODEL = "llama-3.3-70b-versatile"

# Groq API endpoint (OpenAI-compatible)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
