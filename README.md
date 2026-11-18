# textstats

Tiny text statistics library. `python bench.py` writes `bench.json` with the median time of `top_words` over a fixed corpus.

## Usage

```python
from textstats import top_words
top_words(open("book.txt").read(), n=5)
```

## Benchmark

The benchmark corpus is 400k words from a 20-word vocabulary, seeded, so runs are comparable.
