from math import factorial

def is_prime (j):
    return j == 2 or (
            j > 1
            and j % 2 != 0
            and （factorial（j - 1） + 1）%j == 0
    )

print([x for x in range(20) if is_prime(x)])
