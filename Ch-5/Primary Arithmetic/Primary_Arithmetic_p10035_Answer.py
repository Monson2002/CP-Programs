# Name: Monson Reji Verghese
# Problem ID: 10035 
# Class: TY CSE A
# Roll No: 45


import sys
from itertools import zip_longest

def carry_count(num1, num2):
    carry = count = 0
    num1_digits = reversed(list(map(int, list(num1))))
    num2_digits = reversed(list(map(int, list(num2))))
    for d1, d2 in zip_longest(num1_digits, num2_digits, fillvalue=0):
        carry = 1 if d1+d2+carry>9 else 0
        count += carry

    return count

if __name__ == "__main__":
    
    for line in sys.stdin:
        start, end = line.split()[:2]
        if start == '0' and end == '0':
            break

        carry = carry_count(start, end)
        if carry == 0:
            print("No carry operation.")
        elif carry == 1:
            print("1 carry operation.")
        else:
            print("{} carry operations.".format(carry))
    exit(0)
    

# Sample Input
# 123 456
# 555 555
# 123 594
# 0 0

# Sample Output
# No carry operation.
# 3 carry operations.
# 1 carry operation.