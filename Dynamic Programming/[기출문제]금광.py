for t in range(int(input())):
    n, m = map(int, input().split())

    array = list(map(int, input().split()))

    data = []
    index = 0
    for i in range(n):
        data.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = data[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1 :
                left_down = 0
            # 왼쪽에서 오는 경우
            else:
                left_down = data[i+1][j-1]
            left = data[i][j-1]
            data[i][j] = data[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, data[i][m-1])
    print(result)
