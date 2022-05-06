n = int(input())
s = list(map(int, input().split()))
s.sort()

sum = 0
each_time = 0

for i in s:
    each_time += i
    sum += each_time

print(sum)
