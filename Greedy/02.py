# 입력 조건
# 첫 번째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다 (1 <= S의 길이 <= 20)
# 출력 조건
# 첫 번째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다

#23m 52s
#1. 문자열 S를 입력 받는다
#2. 문자열 S의 값을 쪼개서 리스트에 넣는다
#3. 0일 경우 더하기 연산을, 그 외에는 곱 연산을 수행한다
#4. 결과를 출력한다

S = list(input()) #1, 2
S = list(map(int, S))
result = S[0]

for i in range(1, len(S)):
  if result <= 1 or S[i] <= 1:
    result += S[i]
  else:
    result *= S[i]
    
print(result)