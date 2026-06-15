from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from backend.database import Base


# ==========================================
# USERS
# ==========================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(50),
        default="employee"
    )


# ==========================================
# TICKETS
# ==========================================

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func

class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200)
    )

    description = Column(
        Text
    )

    status = Column(
        String(50),
        default="OPEN"
    )

    priority = Column(
        String(50),
        default="MEDIUM"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )


# ==========================================
# KNOWLEDGE BASE
# ==========================================

class KnowledgeBase(Base):

    __tablename__ = "knowledge_base"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    issue = Column(
        String(255),
        nullable=False
    )

    cause = Column(
        Text
    )

    solution = Column(
        Text
    )

    category = Column(
        String(100)
    )


# ==========================================
# CHAT HISTORY
# ==========================================

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer
    )

    query = Column(
        Text
    )

    response = Column(
        Text
    )