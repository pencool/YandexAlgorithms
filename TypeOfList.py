import sys


def list_type():
    answer = ''
    check = float('-inf')
    for i in sys.stdin:
        if i == -2 * (10 ** 9):
            return answer
        if i > check:
            check = i
