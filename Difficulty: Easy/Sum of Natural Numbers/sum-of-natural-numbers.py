import sys
sys.setrecursionlimit(20000)

n = int(input())

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(n))