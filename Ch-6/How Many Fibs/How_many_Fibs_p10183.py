# Name: Monson Reji Verghese
# Problem ID: 10183 
# Class: TY CSE A
# Roll No: 45


import _bisect
def fib(a, b):
    while b < 10**100:
        yield a
        a, b = b, a+b
Fib = list(fib(1, 2))

while True:
    l, h = map(int, input().split())
    if l == 0 and h == 0:
        break
    left = _bisect.bisect_left(Fib, l)
    right = _bisect.bisect_right(Fib, h)
    print(right - left)
    


# Sample Input
# 10 100
# 1234567890 9876543210
# 0 0

# Sample Output
# 5
# 4