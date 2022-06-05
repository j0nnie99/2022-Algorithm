from itertools import combinations

# 입력 N(데이터의 수), K(큰 수 차례)
N, K = map(int, input().split())
data = list(map(int, input().split()))
result = []

# 3개의 조합 구하기 + sum 처리 해서 리스트에 넣기
case = list(combinations(data, 3))  # 3개를 뽑는 모든 조합 구하기
for tmp in case:     # 각 조합의 합을 result에 저장
    result.append(sum(tmp))

result.sort(reverse=True)   # 큰 수부터 정렬

print(result[K-1])
