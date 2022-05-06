# 숫자 카드 게임

N, M = map(int, input().split())

result = 0

for i in range(N):
    number = list(map(int, input().split()))
    mini = min(number)
    result = max(result, mini)

print(result)