import sys
input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num.sort()
print(*num, sep='\n')
