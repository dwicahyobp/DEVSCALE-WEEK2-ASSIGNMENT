import os
from openai import OpenAI
from app.settings import settings
from app.prompts import SYSTEM_PROMPT

def generate_response(prompt: str) -> str:
    client = OpenAI(api_key=settings.openai_api_key)

    completion = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT},{"role": "user", "content": prompt}],
    )

    response = completion.choices[0].message.content
    return response or "Input your Open AI API Key"