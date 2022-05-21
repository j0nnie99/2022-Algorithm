def solution(p):
      return recursion(p)
 
def recursion(w):
    if w == '':  # 1
        return ''

    cnt_open = 0
    cnt_close = 0
    idx = len(w)

    for i in range(len(w)):
        if cnt_open == cnt_close > 0:
            idx = i 
            break
        if w[i] == '(':
            cnt_open += 1
        elif w[i] == ')':
            cnt_close += 1

    u = w[:idx]  # 2
    v = w[idx:]

    if w[0] == '(': # 3
        return u + recursion(v)

    else: # 4
        temp = ''

        for x in u[1:-1]:
            if x == ')':
                temp += '('
            else:
                temp += ')'

        return '(' + recursion(v) + ')' + temp
