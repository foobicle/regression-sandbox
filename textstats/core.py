import re
from collections import Counter

WORD = re.compile(r"[A-Za-z']+")


def tokenize(text):
    return WORD.findall(text)


def normalize(word):
    """Lowercase a word for counting."""
    return word.lower()


def top_words(text, n=10):
    """The n most common normalized words in text."""
    counts = Counter(normalize(w) for w in tokenize(text))
    return counts.most_common(n)

def unique_words(text):
    return sorted({normalize(w) for w in tokenize(text)})

def word_lengths(text):
    return Counter(len(w) for w in tokenize(text))
