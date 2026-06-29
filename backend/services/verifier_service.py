import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def verify_answer(answer: str) -> dict:
    """
    Sends the LLM answer to Groq for hallucination scoring.
    Returns hallucination_score (0-100) and a reason string.
    """
    prompt = f"""You are a hallucination detection expert.

Given the following AI-generated answer, rate how likely it contains hallucinated or made-up information.

Answer to evaluate:
\"\"\"{answer}\"\"\"

Respond with ONLY a JSON object in this exact format, nothing else:
{{"hallucination_score": <number between 0 and 100>, "reason": "<one sentence explanation>"}}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown code fences if model wraps response in them
    if raw.startswith("```"):
        raw = raw.strip("`").strip()
        if raw.startswith("json"):
            raw = raw[4:].strip()

    try:
        result = json.loads(raw)
        # Validate expected keys are present
        if "hallucination_score" not in result or "reason" not in result:
            raise ValueError("Missing expected keys in response")
        return result
    except (json.JSONDecodeError, ValueError):
        return {
            "hallucination_score": 50,
            "reason": "Could not parse verifier response."
        }