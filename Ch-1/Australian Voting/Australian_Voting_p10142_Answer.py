import sys

lines = iter(sys.stdin.read().splitlines())

cases_n = int(next(lines))
cases_results = []

for _ in range(cases_n):
    for line in lines:
        if line.isdigit():
            candidates_n = int(line)
            break
    
    candidates_list = [next(lines) for _ in range(candidates_n)]
    
    votes = []
    for i, line in enumerate(lines):
        vote = line.split()
        if not vote:
            if not line:
                break
        elif i < 1000:
            votes.append(list(map(lambda x: int(x)-1 , vote)))
    
    winners = []
    pos_president = [True]*candidates_n
    
    while not winners:
        counter = [0]*candidates_n
        for vote in votes:
            counter[vote[0]] += 1
    
        max_value = max([count for i, count in enumerate(counter) if pos_president[i]])
        if max_value > len(votes)/2.0:
            max_index = counter.index(max_value)
            winners.append(candidates_list[max_index])
            continue

        min_value = min([count for i, count in enumerate(counter) if pos_president[i]])
        if max_value == min_value:
            for i, posible in enumerate(pos_president):
                if posible:
                    winners.append(candidates_list[i])
        else:
            for i, count in enumerate(counter):
                if pos_president[i] and count == min_value:
                    pos_president[i] = False
                    for vote in votes:
                        vote.remove(i)
    
    cases_results.append('\n'.join(winners))

print('\n\n'.join(cases_results))