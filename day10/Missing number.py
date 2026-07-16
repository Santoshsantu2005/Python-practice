lst = list(map(int, input().split()))

n = len(lst) + 1

for i in range(1, n + 1):
    if i not in lst:
        print(i)
