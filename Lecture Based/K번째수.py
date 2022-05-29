# 첫 줄: 테스트 케이스 개수(T)
T = int(input())

# 결과 출력용 리스트
numbers = []

# 테스트 케이스 input 받기 (N, s, e, k / N개의 수)
for i in range(T):
    tmp = [] # tmp 초기화
    N, s, e, k = map(int, input().split())
    tmp = list(map(int, input().split()))   # N개의 수 입력 받기
    tmp = tmp[s-1:e] # s부터 e만 저장
    tmp.sort() # 오름차순 정렬
    numbers.append(tmp)     # 결과만 따로 저장 (출력용)


for i in range(T):
    print("#" + str(i+1) + " "+ str(numbers[i][k-1])) # 테스트 케이스별로 k번째(리스트 내 k-1번째) 숫자 출력
