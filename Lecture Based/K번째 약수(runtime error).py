# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
# [입력]
# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N이하이다.
# [출력]
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서
# K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오

# 입력
N, K = map(int, input().split())
measure = []

for i in range(1, N+1):
    if N % i == 0:
        measure.append(i)
    else:
        continue

print(measure[K-1])
