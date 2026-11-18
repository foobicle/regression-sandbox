import re
from collections import Counter

WORD = re.compile(r"[A-Za-z']+")


def tokenize(text):
    return WORD.findall(text)


def normalize(word):
    return word.lower()


def top_words(text, n=10):
    """The n most common normalized words in text."""
    counts = Counter(normalize(w) for w in tokenize(text))
    return counts.most_common(n)
