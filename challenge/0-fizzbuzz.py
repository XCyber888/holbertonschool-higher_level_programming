#!/usr/bin/env python3
import sys
def fizzbuzz(n):
    if n < 1: return
    out = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: out.append("FizzBuzz")
        elif i % 3 == 0: out.append("Fizz")
        elif i % 5 == 0: out.append("Buzz")
        else: out.append(str(i))
    print(" ".join(out))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try: fizzbuzz(int(sys.argv[1]))
        except ValueError: sys.exit(1)
