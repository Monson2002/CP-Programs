# Name: Monson Reji Verghese
# Problem ID: 701
# Class: TY CSE A
# Roll No: 45


import math
def num_length(n):
    return int(math.log10(n)) + 1

while True:
    try:
        n = int(input())
        length = num_length(n)
        i = 0
        while True:
            i += 1
            a = math.log2(n) + (length + i) * math.log2(10)
            b = math.log2(n + 1) + (length + i) * math.log2(10)

            temp1 = int(a)
            temp2 = int(b)

            if temp2 != b and temp2 - temp1 > 0:
                print(temp2)
                break

    except EOFError:
        break
