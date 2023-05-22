t = int(input())
while t > 0:
    l = list(map(int, input().split()))
    l = l[1:]
    l.sort()
    median = 0
    if len(l) % 2 == 0:
        median = (l[len(l)//2 - 1] + l[len(l)//2]) // 2
    else:
        median = l[len(l)//2]
    sm = 0
    for i in l:
        sm += abs(i - median)
    print(sm)
    t -= 1
