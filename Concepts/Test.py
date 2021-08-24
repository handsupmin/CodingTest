# Test.py
# 실험용 파일입니다.


from collections import deque

def solution(priorities, location):
    q = deque()
    count = 0
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while q:
        j = q.popleft()
        print(j, max(q))
        if j[0] >= max(q)[0]:
            count += 1
            if j[1] == location:
                return count
        else:
            q.append(j)

print(solution([2, 1, 3, 2],	2))