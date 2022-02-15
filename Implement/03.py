from itertools import combinations

#print(chr(ord('h') + 1))

loc = list(input())
x = ord(loc[0])
y = int(loc[1])

count = 0
# y < 1 or y > 8 (X)
# x < ord('a') or x > ord('h') (X)


for i in range(8):  # 8개의 경우의 수에 대해
  # x는 어떻게 되고
  # y는 어떻게 되고
  if x < ord('a') or x > ord('h') or y < 1 or y > 8 :
    continue
  else:
    count += 1