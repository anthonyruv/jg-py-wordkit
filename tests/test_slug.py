from wordkit import slugify


def test_slugify_lowercases_and_replaces_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_separators_and_trims_hyphens():
    assert slugify("  --a--b--  ") == "a-b"


def test_slugify_empty_string():
    assert slugify("") == ""
