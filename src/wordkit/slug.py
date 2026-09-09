"""Utilities for creating URL-friendly slugs."""

import re


def slugify(text: str) -> str:
    """Convert text to a lowercase, ASCII-alphanumeric slug."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
