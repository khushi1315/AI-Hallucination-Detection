from sqlalchemy import Column, Integer, String, Text, Float
from database.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    question = Column(Text)
    response = Column(Text)


class VerificationResult(Base):
    __tablename__ = "verification_results"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    hallucination_score = Column(Float)
    explanation = Column(Text)


class Claim(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True)
    verification_id = Column(Integer)
    claim = Column(Text)
    status = Column(String)
    confidence = Column(Float)