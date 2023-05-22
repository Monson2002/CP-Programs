# Name: Monson Reji Verghese
# Problem ID: 10037 
# Class: TY CSE A
# Roll No: 45


import sys
from heapq import  heappush, heappop, heapify

BEFORE = True
AFTER = False

def load_num():
    line = sys.stdin.readline()
    if line == ' ' or line == '\n':
        return None

    return int(line)

def load_case():
    npeople = load_num()
    people = []
    for p in range(npeople):
        people.append(load_num())

    return people


def get_cross_candidates(before):

    candidates = []
    l = len(before)
    if l > 3:
        t1 = before[1]+before[0]+before[l-1]+before[1]
        t2 = before[l-1]+before[0]+before[l-2]+before[0]
        if t1 <= t2:
            candidates = [
                    (before[0], before[1]), 
                    (before[0],), 
                    (before[l-2], before[l-1]), 
                    (before[1],)]
        else:
            candidates = [
                    (before[0], before[l-2]),
                    (before[0],), 
                    (before[0], before[l-1]),
                    (before[0],)]  
        before.pop()
        before.pop()
    elif l == 3:
        candidates = [
                (before[0], before[1]), 
                (before[0],), 
                (before[0], before[2])]
        before[:] = []     
    elif l == 2:
        candidates = [(before[0], before[1])]
        before[:] = []
    
    else:
        candidates = [(before[0],)]
        before[:] = []

    return candidates


def cross_strat(people):

    order = []
    before = sorted(people)
    seconds = 0

    while len(before):
        candidates = get_cross_candidates(before)
        for c in candidates:
            seconds += max(c)
            order.append(c)

    return seconds, order

if __name__ == '__main__':

    cases = load_num()
    for c in range(cases):
        sys.stdin.readline()
        people = load_case()
        seconds, order = cross_strat(people)
        print(seconds)
        for p in order:
            print(" ".join(map(str, p)))
        if c<cases-1: 
            print('')


# Sample Input
# 1
# 4
# 1
# 2
# 5
# 10
# Sample Output
# 17
# 1 2
# 1
# 5 10
# 2
# 1 2