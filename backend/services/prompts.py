def get_system_prompt() -> str:
    """
    System prompt — tells the AI who it is and how to behave.
    This runs at the start of every conversation.
    """
    return """You are a helpful and accurate AI assistant.
Answer questions clearly and concisely.
If you are unsure about something, say so honestly.
Do not make up facts or hallucinate information."""


def get_chat_prompt(question: str) -> str:
    """
    Kept for backward compatibility.
    Used only if history is not available.
    """
    return f"""You are a helpful and accurate AI assistant.
Answer the following question clearly and accurately.

Question: {question}

Answer:"""