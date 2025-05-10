import sys

if len(sys.argv) > 2:
    print("Error: This script accepts only one argument — the path to the book file to analyze.\n")
    print("Example usage:\n  python3 main.py books/ToKillAMockingBird.txt")
else:
    print(sys.argv[1])