# Q111.py
# https://www.acmicpc.net/problem/3052

result = set()

for i in range(10):
    result.add(int(input()) % 42)

print(len(result))