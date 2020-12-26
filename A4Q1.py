import sys

def fourteen_queen(pos):
    n = 14
    given = {k:v for k,v in pos}
    #compile cols and diagonals due to given queens
    reject = setup(given)
    #compile possible positions for each row after eliminating the cols and diagonals of given queens 
    pool = {}
    for i in range(1,n+1):
        if i in given.keys():
            pool[i] = [given[i]]
        else:
            pool[i] = [j for j in range(1,n+1) if j not in reject[i]]
    pool = [v for v in pool.values()]
    #count number of possible positions based on reduced pool of possibilities
    return count(pool)    
           


def count(pool, prefix=[], majdiag=[], mindiag=[]):
    x = 0
    #if reach the last row and col of last row does not cause any conflict, add 1 to the count
    if not pool:
        return 1
    #recursion to generate all permutations of cols 
    first = pool[0]
    rest = pool[1:]
    for num in first:
        #check that current col is not already taken by previous rows
        if num not in prefix:
            #check that current position does not clash with the diagonals of queens placed in previous rows
            if len(prefix)+1-num not in majdiag and len(prefix)+1+num not in mindiag:
                x += count(rest, prefix + [num], majdiag+[len(prefix)+1-num], mindiag+[len(prefix)+1+num])
    return x
          
def setup(given):
    reject = {}
    #find diagonals of given queens
    for k,v in given.items():
        cnt = 1
        for i in range(k-1,0,-1):
            reject[i] = reject.get(i, []) + [v-cnt,v+cnt]
            cnt += 1
        cnt = 1
        for i in range(k+1,15):
            reject[i] = reject.get(i, []) + [v-cnt,v+cnt]
            cnt += 1
    existing = [v for k,v in given.items()]
    #compile cols and diagonals due to given queens
    for k,v in reject.items():
        v += existing
    for k,v in reject.items():
        if v:
            reject[k] = [i for i in set(v) if 0<i<(14+1)]
    return reject


num_case = int(sys.stdin.readline())
for _ in range(num_case):
    s = sys.stdin.readline().split()
    n, pos = len(s) // 2, []
    for i in range(n):
        pos.append((int(s[2*i]), int(s[2*i+1])))
    print(fourteen_queen(pos))


