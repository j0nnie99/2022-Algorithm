# 1.모험가 수, 공포도 입력
N = int(input())
group = list(map(int, input().split()))
group.sort()

result = 0
current = 1

# 2."현재 그룹에 포함된 모험가의 수 >= 현재 확인하고 있는 공포도"일 경우 그룹 생성
for i in group:
  if current >= i: 
    result += 1
    current = 1
  else:
    current += 1

print(result)