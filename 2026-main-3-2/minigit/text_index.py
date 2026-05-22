"""Text normalization helpers for Mini Git search indexes."""

from __future__ import annotations


def normalize_token(token: str) -> str:
    """Normalize user text and message keywords for case-insensitive lookup."""
    return token.strip().lower()


def split_message_keywords(message: str) -> list[str]:
    """Split a commit message into normalized keyword tokens."""
    tokens = []
    seen = set()
    for raw in message.split():
        token = normalize_token(raw)
        if token and token not in seen:
            seen.add(token)
            tokens.append(token)
    return tokens
