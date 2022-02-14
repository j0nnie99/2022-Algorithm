# N, K를 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k # N이 K로 나누어 떨어지지 않을 때 N에 가장 가까운 나누어 떨어지는 수 찾기 -> 1을 몇 번 빼야하는지 확인 가능
    result += (n - target) # n - target = 1이 반복되는 횟수 -> result 값에 넣어주기
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
result += (n - 1)
print(result)
