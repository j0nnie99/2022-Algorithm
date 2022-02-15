# 미완성

N = int(input())
list = []
for i in range(60):
  list.append(i)

count = 0

for i in list:
  if i % 10 == 3:
    count += 1
    
print(count)
# N에 3이 있을 때 (N % 10 == 3)
if N % 10 == 3:
  N * 60
else:  # N에 3이 없을 때
  (N - 1) * count
  