n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

#플로이드 워셜 알고리즘(Floyd Warshall Algorithm) 이용
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i]) # * : 리스트 각각의 값을 출력 가능
