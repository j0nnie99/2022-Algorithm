# 1. 맵과 가본 좌표 업데이트 하는 array를 별도로 2개 만듦
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
move_array = [[0] * m for _ in range(n)]  # 기본 좌표 저장하기 위한 array
move_array[x][y] = 1  # 첫 좌표

# 맵 정보
map_array = []
for _ in range(n):
    data = list(map(int, input().split()))
    map_array.append(data)

# 방향 좌표(인덱스 = 방향이랑 동일하게)리스트 생성
# 서, 북, 동, 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 바꾸는 함수
def change_direction():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

count = 1  # 방문한 칸 횟수(출력할 것)
dir_count = 0  # 몇 번 방향을 바꾸었는지(4되면 한 바퀴)
while True:
    change_direction()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if move_array[nx][ny] == 0 and map_array[nx][ny] == 0:
        move_array[nx][ny] = 1
        x, y = nx, ny
        count += 1
        dir_count = 0
        continue
    else:
        dir_count += 1
    # 방향 4번 모두 바꿨을 때
    if dir_count == 4:
        # 바라보던 방향으로 다시 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_array[nx][ny] == 0:
            x, y = nx, ny
            dir_count = 0
        else:
            break

print(count)