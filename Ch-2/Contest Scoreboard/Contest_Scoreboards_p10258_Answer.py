from typing import List

class Board:
    def __init__(self, contestant: int) -> None:
        self.contestant = contestant
        self.nproblem = 0
        self.problem = [0]*10
        self.penalty = [0]*10
        self.time = 0
        
    def calc_time(self) -> None:
        for i in range(1, 10):
            if self.problem[i] == 1:
                self.time += self.penalty[i]

def init(index: List[int]) -> None:
    for i in range(101):
        index[i] = -1

def judge(b: Board, problem: int, time: int, L: str) -> None:
    if b.problem[problem] == 1:
        return
    if L == 'C':
        b.nproblem += 1
        b.problem[problem] = 1
        b.penalty[problem] += time
    elif L == 'I':
        b.penalty[problem] += 20

def main() -> None:
    T = int(input())
    input()
    for t in range(1, T+1):
        index = [-1]*101
        v = []
        while True:
            try:
                s = input().strip()
            except:
                break
            if s == "":
                break
            contestant, problem, time, L = map(str, s.split())
            contestant, problem, time = int(contestant), int(problem), int(time)
            if index[contestant] == -1:
                v.append(Board(contestant))
                index[contestant] = len(v) - 1
            judge(v[index[contestant]], problem, time, L)
        for it in v:
            it.calc_time()
        v.sort(key=lambda x: (-x.nproblem, x.time, x.contestant))
        for it in v:
            print(it.contestant, it.nproblem, it.time)
        if t < T:
            print()

if __name__ == '__main__':
    main()