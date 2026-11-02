import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=20000)
)

def generate_insights(metrics):

    prompt = f"""
    You are a Senior Business Data Analyst.

    Analyse these verified business metrics:

    {metrics}

    Provide:
    1. Business performance summary.
    2. Three important business insights.
    3. Best performing city.
    4. Marketing channel performance.
    5. Business opportunities.
    6. Three actionable recommendations.

    Rules:
    - Use only the supplied data.
    - Never invent statistics.
    - Mention data limitations.
    - Distinguish highest conversion rate from highest booking volume.
    - Never recommend increasing marketing spend without cost or ROI data.
    - Do not claim temporal data is missing if booking dates are supplied.
    """

    print("Sending request to Gemini...")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
        max_output_tokens=1500
    )
    )

    print("Gemini response received!")

    return response.text