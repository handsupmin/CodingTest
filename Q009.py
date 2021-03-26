# Q009.py

"""
음료수 얼려먹기
N x M 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려있는 부분끼리 상, 하 , 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 대 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라,
"""

n, m = map(int, input().split())

graph = []

# 2차원 리스트의 맵 정보 받기
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    # 현재 노드를 방문한 적이 없다면
    if graph[x][y] == 0:
        # 현재 노드를 방문처리
        graph[x][y] = 1
        #  상, 하 , 좌, 우에 있는 노드들도 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

# 모둔 위치에 대하여 음료 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""