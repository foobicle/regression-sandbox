"""Benchmark: time top_words over a fixed synthetic corpus. Writes bench.json."""
import json, random, statistics, time
from textstats import top_words

def corpus(seed=7, words=400_000):
    rng = random.Random(seed)
    vocab = ["alpha", "Beta", "gamma", "Delta", "epsilon", "zeta", "eta", "Theta", "iota", "kappa",
             "lambda", "Mu", "nu", "xi", "omicron", "pi", "Rho", "sigma", "tau", "upsilon"]
    return " ".join(rng.choice(vocab) for _ in range(words))

def main():
    text = corpus()
    times = []
    for _ in range(5):
        t = time.perf_counter(); top_words(text); times.append((time.perf_counter() - t) * 1000)
    out = {"benchmark": "top_words_400k", "median_ms": round(statistics.median(times), 1),
           "runs_ms": [round(x, 1) for x in times]}
    json.dump(out, open("bench.json", "w"), indent=2)
    print(json.dumps(out))

if __name__ == "__main__":
    main()
