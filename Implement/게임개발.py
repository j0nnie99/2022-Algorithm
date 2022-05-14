n, m = map(int, input().split())
start_point = map(int, input().split())

map = []
for i in range(n):
    map[i] = list(map(int, input().split()))

# 동서남북
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]


print(n, m, start_point, map)

