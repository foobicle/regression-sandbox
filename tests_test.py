from textstats import tokenize, normalize, top_words

def test_tokenize():
    assert tokenize("Hello, world! It's") == ["Hello", "world", "It's"]

def test_normalize():
    assert normalize("Beta") == "beta"

def test_top_words():
    assert top_words("a b a", 1) == [("a", 2)]
