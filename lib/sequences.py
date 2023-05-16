#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []

    if length == 0:
        print(sequence)
        return

    # Generate the Fibonacci sequence
    a, b = 0, 1
    sequence.append(a)

    while len(sequence) < length:
        sequence.append(b)
        a, b = b, a + b

    # Print the Fibonacci sequence
    print(sequence)
    pass