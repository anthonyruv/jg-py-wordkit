import six


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``."""
    return len(six.ensure_str(text).split())
