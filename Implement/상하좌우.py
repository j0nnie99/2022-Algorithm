n = int(input())
s = list(input().split())

x = 1
y = 1

for i in s:
    if i == "L":
        if y-1 == 0:
            continue
        else:
            y -= 1
    if i == "R":
        if y+1 > n:
            continue
        else:
            y += 1            
    if i == "U":
        if x-1 == 0:
            continue
        else:
            x -= 1
    if i == "D":
        if x+1 > n:
            continue
        else:
            x += 1           

print(x, y)