import time,sys
from collections import deque
start=time.time()

inf = sys.argv[1] if len(sys.argv) > 1 else './day7/input.txt'
with open(inf) as fi:
    a = fi.readlines()

D = dict()
D['root'] = 0
def cd(directory, cmds):
    newfiles = D[directory]
    directories = []
    while cmds:
        C = cmds.pop(0)[:-1].split(' ')
        if C[0] != '$':
            if C[0] == 'dir':
                if directory+C[1] not in D.keys():
                    D[directory+C[1]] = 0
                directories.append(directory+C[1])
            else:
                newfiles += int(C[0])
        elif C[1] == 'cd':
            if C[2] == '..':
                size= newfiles
                for x in directories:
                    size += D[x]
                return size
            else:
                D[directory+C[2]] = cd(directory+C[2],cmds)
    size= newfiles
    for x in directories:
        size += D[x]
    return size

D['root'] = cd('root',a[1:])

summedsize = 0
for x in D.values():
    if x<=100000:
        summedsize +=x
print('part1', summedsize)

possible = []
unused = 70000000 - D['root']
for x in D.values():
    if unused + x >= 30000000:
        possible.append(x)
print('part2',min(possible))

end=time.time()
print(round(end-start,6))