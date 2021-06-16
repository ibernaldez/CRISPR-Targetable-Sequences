"""

Generating CRISPR Targetable Sequences in the Human Genome
refer to doc sent by henri

"""
import sys
def print_lines():
    stdin_stack = []
    for line in sys.stdin:
        stdin_stack.append(line.strip())
    std = stdin_stack[:7]
    count = -1
    for i in std:
        count += 1
        y = i[-2:]
        if y == "gc":

            print("yay!")
            print(i)
            print(count)
    print(std)
print_lines()
