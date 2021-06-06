
from itertools import combinations, permutations
import sys
import time

if __name__ == '__main__':
    T = int(input())
    blank = input()
    resultado = [T]
    while T > 0:
        jornais = []
        datasets = []
        c = input().strip().split()
        tam_jornal = False
        if c[0] != '*':
            for _ in c:
                datasets.append(int(_))
            #print(f'duvida: {datasets} - tipo :{type(datasets)}')
            while True:
                n = input()
                if n == '':
                    break
                else:
                    jornais.append(n)
            if len(datasets) == 2:
                for i in range(min(datasets), max(datasets) + 1):
                    #print(i)
                    print(f'Size {i}')
                    #temp = list(map(set, combinations(jornais, i)))
                    subsets = list(combinations(jornais, i))
                    subsets.sort(key=lambda i: jornais.index(i[0]))
                    for s in subsets:
                        print(', '.join(s))
                    print(end='\n')
            else:
                print(f'Size {len(datasets)}')
                #temp = list(map(set, combinations(jornais, i)))
                subsets = list(combinations(jornais, len(datasets)))
                subsets.sort(key=lambda i: jornais.index(i[0]))
                for s in subsets:
                    print(', '.join(s))
                print(end='\n')
        else:
            while True:
                try:
                    n = input()
                    jornais.append(n)
                except EOFError:
                    break
            for i in range(1, len(jornais) + 1):
                    print(f'Size {i}')
                    subsets = list(combinations(jornais, i))
                    subsets.sort(key=lambda i: jornais.index(i[0]))
                    for s in subsets:
                        print(', '.join(s))
                    print(end='\n')
        T -= 1
