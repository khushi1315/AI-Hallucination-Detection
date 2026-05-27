import os
from groq import Groq
from dotenv import load_dotenv
from services.prompts import get_system_prompt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(question: str, history: list = []) -> str:
    """
    Takes a question + conversation history.
    Builds a full message thread and sends to Groq.
    Returns Llama3's answer as a plain string.
    """
    # Start with the system prompt — sets the AI's behaviour
    messages = [
        {"role": "system", "content": get_system_prompt()}
    ]

    # Add conversation history so the model has context
    for msg in history:
        messages.append({
            "role": msg.role,
            "content": msg.content
        })

    # Add the new question at the end
    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content