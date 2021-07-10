import heapq

def solution(food_times, k):
    answer = 0
    q = []
    num = 0
    n1 = 0
    sum_num = 0
    for value in food_times:
        num += 1
        heapq.heappush(q, (value, num))
    
    temp = heapq.heappop(q)
    n1 = temp[0]
    sum_num += n1 * num
    while True:
        num -= 1
        if num < 0:
            return -1
        if k < sum_num:
            heapq.heappush(q, temp)
            break
        temp = heapq.heappop(q)
        n1 = temp[0] - n1
        sum_num += n1 * num
    
    h = []
    for a in q:
        num += 1
        heapq.heappush(h, (a[1], a[0]))
    
    answer = h[k%num][0]
    
    return answer