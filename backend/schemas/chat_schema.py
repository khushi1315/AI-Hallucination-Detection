from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str       # "user" or "assistant"
    content: str    # the message text

class ChatRequest(BaseModel):
    question: str
    history: Optional[List[Message]] = None  # empty by default