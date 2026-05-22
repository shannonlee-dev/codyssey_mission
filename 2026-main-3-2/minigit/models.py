"""Data models for Mini Git."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Commit:
    """A commit node in the Mini Git DAG."""

    hash: str
    message: str
    author: str
    timestamp: str
    parents: list[str]
    branches: list[str]
