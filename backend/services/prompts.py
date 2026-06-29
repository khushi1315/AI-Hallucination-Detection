def get_system_prompt() -> str:
    """
    System prompt — tells the AI who it is and how to behave.
    Emotion detection removed.
    """
    return (
        "You are a helpful and accurate AI assistant. "
        "Do not make up facts or hallucinate information. "
        "If you are unsure about something, say so honestly."
    )


def get_chat_prompt(question: str) -> str:
    """
    Fallback prompt if history is unavailable.
    """
    return f"""You are a helpful and accurate AI assistant.
Answer the following question clearly and accurately.

Question: {question}

Answer:"""