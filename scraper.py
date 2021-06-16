"""

Generating CRISPR Targetable Sequences in the Human Genome
refer to doc sent by henri

"""
import sys
def print_lines():
    stdin_stack = []
    for line in sys.stdin:
        stdin_stack.append(line.strip())
    count = -1
    for i in stdin_stack:
        count += 1
        y = i[-2:]
        if y == "gc":

            print("yay!")
            print(i)
            print(count)
print_lines()
