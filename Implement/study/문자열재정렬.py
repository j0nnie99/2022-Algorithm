s = list(input())
s.sort()

# list로 받았더니 숫자도 str형으로 들어온다
# 문자와 숫자를 구분해줄 수 있는 방법이 없을까 -> isdigit(), isalpha()

answer = []
sum = 0

for i in s:
    if i.isdigit(): # 숫자일 경우 int형으로 반환 후 sum
        i = int(i)
        sum += i
    elif i.isalpha(): # 문자일 경우 결과값으로 출력할 리스트에 append
        answer.append(i)
    else:
        continue

answer = ''.join(answer) # 리스트 출력을 문자열처럼 이어서 출력되도록 join 함수 사용
print(answer + str(sum))