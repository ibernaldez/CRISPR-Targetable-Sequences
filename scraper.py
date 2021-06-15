"""

Generating CRISPR Targetable Sequences in the Human Genome
refer to doc sent by henri

"""
import sys
def print_lines():
    stdin_stack = []
    for line in sys.stdin:
        stdin_stack.append(line.strip())
    print(stdin_stack[:20] + ["/n"])
print_lines()
