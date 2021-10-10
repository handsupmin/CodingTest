# Test.py
# 실험용 파일입니다.

from collections import defaultdict
from collections import deque

def solution(enroll, referral, seller, amount):
    list_dict = defaultdict(list)
    cost_dict = defaultdict(int)
    
    for i in range(len(enroll)):
        cost_dict[enroll[i]] = 0
        if referral[i] != '-':
            list_dict[enroll[i]].append(referral[i])
    
    for i in range(len(seller)):
        who = seller[i]
        much = amount[i] * 100
        
        queue = deque()
        queue.append(who)
        while queue:
            now = queue.popleft()
            left = int(0.1 * much)
            if much < 10:
                cost = much
                cost_dict[now] += cost
                break
            else:
                cost = much - left
            much = left
            cost_dict[now] += cost
            nxt = list_dict[now]
            if len(nxt):
                nxt = nxt[0]
                queue.append(nxt)
            else:
                break
    
    result = []
    for person in enroll:
        result.append(cost_dict[person])
    
    return result

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	,["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))