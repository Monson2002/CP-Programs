# Name: Monson Reji Verghese
# Problem ID: 10041 
# Class: TY CSE A
# Roll No: 45


no_case = int(input())

while (no_case):

    temp = input().split(" ")
    print(temp)
    r = temp[0]
    temp.remove(r)
    r = int(r)

    for i in range(0, r):
        temp[i] = int(temp[i])

    temp.sort()
    mid = temp[r // 2]
    ans = 0
    for i in temp:
        ans += abs(i - mid)

    print(ans)
    no_case -= 1
    
    
# Sample Input
# 2
# 2 2 4
# 3 2 4 6

# Sample Output
# 2
# 4