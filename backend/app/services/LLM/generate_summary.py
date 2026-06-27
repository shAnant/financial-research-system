from google import genai
from dotenv import load_dotenv
import json
import os
from services.LLM.llm_prompt import get_prompt
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)
client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

def summary(stock_name):
    model = "gemini-2.5-flash"
    message = get_prompt(stock_name)
    response = client.models.generate_content(
        model = model, contents=message
    )
    try:
        cleaned = response.text.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

        data = json.loads(cleaned)

        return data

    except json.JSONDecodeError as e:
        return e
    