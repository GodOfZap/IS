#!/usr/bin/env python3
import sys
import argparse
from typing import Iterable


def _try_composite(a: int, d: int, n: int, s: int) -> bool:
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True


def is_probable_prime(n: int, bases: Iterable[int]) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:
        if a % n == 0:
            return True
        if _try_composite(a, d, n, s):
            return False
    return True


def is_prime(n: int, rounds: int = 5) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    if n < 2**64:
        bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
        return is_probable_prime(n, bases)

    default_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23][:rounds]
    return is_probable_prime(n, default_bases)


def parse_input(prompt: str = "Enter number to test primality: ") -> int:
    while True:
        try:
            s = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        s = s.strip()
        if not s:
            print("Please enter a number.")
            continue
        try:
            n = int(s)
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Primality test (Miller–Rabin)")
    parser.add_argument("number", nargs="?", help="integer to test", type=int)
    parser.add_argument("-r", "--rounds", help="number of MR rounds for large numbers (default 5)", type=int, default=5)
    args = parser.parse_args()

    if args.number is None:
        n = parse_input()
    else:
        n = args.number

    result = "Prime" if is_prime(n, rounds=args.rounds) else "Not Prime"
    print(f"Primality Test Result: {result}")


if __name__ == "__main__":
    main()
##################################################
# Example Output:
#Enter number to test primality: 97
#Primality Test Result: Prime
##################################################