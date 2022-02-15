S = list(input())
S.sort()
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

result = ""
result_num = 0

for i in S:
  if i in numbers:
    result_num += int(i)
  else:
    result += i

print(result + str(result_num))