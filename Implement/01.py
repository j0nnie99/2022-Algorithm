N = int(input())
plan = list(input().split())

# 현재 위치
x, y = 1, 1

for i in plan:
  if i == "R":
    if y == N:
      continue
    else:
      y += 1
  elif i == "L":
    if y == 1:
      continue
    else:
      y -= 1
  elif i == "U":
    if x == 1:
      continue
    else:
      x -= 1
  elif i == "D":
    if x == N:
      continue
    else:
      x += 1
  else:
    "Wrong Direction!"
    
print(x, y)
    