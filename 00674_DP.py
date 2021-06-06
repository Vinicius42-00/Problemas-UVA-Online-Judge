# Coin Change
import sys
import datetime
from functools import lru_cache

def get_input_list():
    montante = []
    while True:
        try:
            n = int(input())
            montante.append(n)
        except ValueError: break
        #finally:
    return montante

def listToTuple(function):
    def wrapper(*args):
        args = [tuple(x) if type(x) == list else x for x in args]
        result = function(*args)
        result = tuple(result) if type(result) == list else result
        return result
    return wrapper

valor_max = 7489

@listToTuple
@lru_cache(maxsize=100000000)
def solve(S, m, n):
    tabela = [0 for k in range(n+1)]
    tabela[0] = 1
    if tabela[n] != 0:
        return tabela[n]
    else:
        for i in range(0,m):
            for j in range(S[i],n+1):
                tabela[j] += tabela[j-S[i]]
    return tabela[n]


if __name__ == '__main__':
    #inicio = datetime.datetime.now()
    #montantes = get_input_list()
    montante = []
    while True:
        try:
            n = int(sys.stdin.readline())
            montante.append(n)
        except Exception: break
    moedas = [1, 5, 10, 25, 50]
    for m in montante:
        if m > valor_max:
            m = valor_max
        else:
            print(solve(moedas, len(moedas), m))
    #fim = datetime.datetime.now()
    #print(fim - inicio)

