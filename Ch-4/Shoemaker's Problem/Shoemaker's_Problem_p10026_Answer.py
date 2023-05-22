# Name: Monson Reji Verghese
# Problem ID: 10026 
# Class: TY CSE A
# Roll No: 45


import sys

class Shoe(object):

    def __init__(self, sid, time, fine):
        self.sid = sid
        self.time = time
        self.fine = fine

    def __lt__(self, oshoe):
        return self.time*oshoe.fine < self.fine*oshoe.time

    def __str__(self):
        return "Shoe({}, {}, {})".format(self.sid, self.time, self.fine)

def load_num():
    line = sys.stdin.readline()
    if line == '' or line == '\n':
        return None

    return list(map(int, line.rstrip().split()))

def load_case():
    sys.stdin.readline()
    nshoes = load_num()[0]
    shoes = []
    for n in range(nshoes):
        time, fine = load_num()
        shoes.append(Shoe(n+1, time, fine))

    return shoes

def schedule_shoes(shoes):
    return [s.sid for s in sorted(shoes)]

if __name__ == "__main__":
    
    ncases = load_num()[0]

    for c in range(ncases):
        sched = schedule_shoes(load_case())

        print(" ".join([str(s) for s in sched]))

        if c + 1 < ncases:
            print('')

    

# Sample Input
# 1
# 4
# 3 4
# 1 1000
# 2 2
# 5 5

# Sample Output
# 2 1 3 4