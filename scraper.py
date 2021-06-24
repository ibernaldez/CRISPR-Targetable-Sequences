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
        for j in range(len(i)):
            count += 1
            y = i[j]
            try:
                x = i[j+1]
            except IndexError:
                x = i[j]

            if y == "g" and x =="c":
                print("Position:" + str(count))
                print(i)
print_lines()
