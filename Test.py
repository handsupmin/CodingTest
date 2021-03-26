# Test.py
# 실험용 파일입니다.

import time
start = time.time()  # 시작 시간 저장
array = [7, 8, 5, 9, 0, 3, 1, 6, 2, 4, 8, 8]
result = []

result.append(array[0])
index = 0

for i in range(1, len(array)):
    for j in range(0, i):
        if array[i] <= result[0]:
            index = 0
        elif array[i] > result[len(result)-1]:
            index = len(result)
        elif result[j] <= array[i] < result[j+1]:
            index = j+1
    result.insert(index, array[i])

print(result)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
