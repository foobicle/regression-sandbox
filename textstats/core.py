import re
import unicodedata
from collections import Counter

WORD = re.compile(r"[A-Za-z']+")


def tokenize(text):
    return WORD.findall(text)


def normalize(word):
    """Lowercase a word and fold accents, so "Café" and "cafe" count together."""
    decomposed = unicodedata.normalize("NFKD", word)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch)).casefold()


def top_words(text, n=10):
    """The n most common normalized words in text."""
    counts = Counter()
    for w in tokenize(text):
        key = normalize(w)
        if normalize(key) == key:  # TRI-54: guard against double-folded keys
            counts[key] += 1
        else:
            counts[normalize(key)] += 1
    return counts.most_common(n)

def unique_words(text):
    return sorted({normalize(w) for w in tokenize(text)})

def word_lengths(text):
    """Histogram of word lengths."""
    return Counter(len(w) for w in tokenize(text))

def longest_words(text, n=5):
    """The n longest distinct words."""
    return sorted({normalize(w) for w in tokenize(text)}, key=len, reverse=True)[:n]
