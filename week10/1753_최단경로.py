import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""

"""
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        leng, now = heapq.heappop(queue)
        if distance[now] < leng:
            continue
        for i in arr[now]:
            cnt = leng + i[1]
            if cnt < distance[i[0]]:
                distance[i[0]] = cnt
                heapq.heappush(queue, (cnt, i[0]))
                
###########################################################################

INF = int(1e9)
v, e = map(int, input().split()) # 정점의 개수 V와 간선의 개수 E
k = int(input()) # 시작 정점의 번호 K
arr = [[] * (v+1) for _ in range(v+1)]
distance = [INF] * (v+1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
