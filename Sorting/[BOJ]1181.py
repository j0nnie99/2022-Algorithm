N = int(input())
#중복제외: set
w = set(input()for _ in range(N))
words = list(w)

# 사전순으로 정렬
words.sort()
# print(words)
# 길이순으로 정렬
words.sort(key=len)
# print(words)

for i in range(len(words)):
    print(words[i])
