import random
import math
from bigram_utils import plausibility

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_")

def decrypt(ciphertext: str, key: str) -> str:
    table = str.maketrans("".join(ALPHABET), key)
    return ciphertext.translate(table)

def random_key() -> str:
    key = ALPHABET.copy()
    random.shuffle(key)
    return "".join(key)

def mutate(key: str) -> str:
    key = list(key)
    a, b = random.sample(range(len(key)), 2)
    key[a], key[b] = key[b], key[a]
    return "".join(key)

def prolom_substitute(ciphertext: str, TM_ref, iter: int = 100000) -> tuple[str, str, float]:
    best_key = random_key()
    best_plain = decrypt(ciphertext, best_key)
    best_score = plausibility(best_plain, TM_ref)

    current_key = best_key
    current_score = best_score

    for i in range(iter):
        new_key = mutate(current_key)
        new_plain = decrypt(ciphertext, new_key)
        new_score = plausibility(new_plain, TM_ref)

        if new_score > current_score or math.exp(new_score - current_score) > random.random():
            current_key = new_key
            current_score = new_score

            if new_score > best_score:
                best_key = new_key
                best_score = new_score
                best_plain = new_plain

        if i % 5000 == 0:
            print(f"Iteration {i}, score: {best_score}")

    return best_key, best_plain, best_score
