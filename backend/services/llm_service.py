import os
from groq import Groq
from dotenv import load_dotenv
from services.prompts import get_system_prompt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(question: str, history: list = None) -> str:
    """
    Takes a question + conversation history.
    Builds a full message thread and sends to Groq.
    Returns Llama3's answer as a plain string.
    """
    if history is None:
        history = []

    messages = [
        {"role": "system", "content": get_system_prompt()}
    ]

    for msg in history:
        # Handles both Pydantic objects and plain dicts safely
        if isinstance(msg, dict):
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        else:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content