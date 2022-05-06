# 큰 수의 법칙

N, M, K = map(int,input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = numbers[N - 1]
second = numbers[N - 2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)