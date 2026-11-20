from textstats import tokenize, normalize, top_words

def test_tokenize():
    assert tokenize("Hello, world! It's") == ["Hello", "world", "It's"]

def test_normalize():
    assert normalize("Beta") == "beta"

def test_top_words():
    assert top_words("a b a", 1) == [("a", 2)]

def test_unique_words():
    from textstats import unique_words
    assert unique_words("B a b") == ["a", "b"]

def test_word_lengths():
    from textstats import word_lengths
    assert word_lengths("ab abc ab")[2] == 2

def test_normalize_folds_accents():
    assert normalize("Café") == "cafe"

def test_top_words_n():
    assert len(top_words("a b c d", 2)) == 2

def test_longest_words():
    from textstats import longest_words
    assert longest_words("a abc ab", 1) == ["abc"]


def test_sentence_count():
    from textstats.core import sentence_count
    assert sentence_count("One. Two! Three?") == 3
