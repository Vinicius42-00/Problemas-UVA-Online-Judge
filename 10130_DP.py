#SuperSale
from functools import lru_cache
import sys
import datetime

#Custom Decorator function - https://stackoverflow.com/questions/49210801/python3-pass-lists-to-function-with-functools-lru-cache
def listToTuple(function):
    def wrapper(*args):
        args = [tuple(x) if type(x) == list else x for x in args]
        result = function(*args)
        result = tuple(result) if type(result) == list else result
        return result
    return wrapper



def knapsack_FR(p, v, cmax):
    n = len(p)
    opt = [[0] * (cmax + 1) for _ in range(n + 1)]
    sel = [[False] * (cmax + 1) for _ in range(n + 1)]
    # Caso Base
    for cap in range(p[0], cmax + 1):
        opt[0][cap] = v[0]
        sel[0][cap] = True
    # Inducao
    for i in range(1, n):
        for cap in range(cmax + 1):
            if cap >= p[i] and opt[i-1][cap - p[i]] + v[i] > opt[i-1][cap]:
                opt[i][cap] = opt[i-1][cap - p[i]] + v[i]
                sel[i][cap] = True
            else:
                opt[i][cap] = opt[i-1][cap]
                sel[i][cap] = False
    # Solucao
    cap = cmax
    solution = []
    for i in range(n - 1, -1, -1):
        if sel[i][cap]:
            solution.append(i)
            cap -= p[i]
    return (opt[n - 1][cmax], solution)

@listToTuple
@lru_cache(maxsize=10000)
def solve(precos, pesos, cargas):
    #numero_obj, precos, pesos, pessoas, cargas = param
    valor_max = 0
    memo = []
    for w in cargas:
        #valor_max += MF_knapsack(len(pesos), pesos, precos, w)
        valor_max += knapsack_FR(pesos, precos, w)[0]
        memo.append(valor_max)
    resultado = str(valor_max)
    return ''.join(resultado)


if __name__ == '__main__':
    #inicio = datetime.datetime.now()
    T = int(sys.stdin.readline())
    if T < 1: T = 1
    if T > 1000: T = 1000
    #print(T)
    while T > 0:
        numero_objetos = int(input())
        pesos = []
        precos = []
        n = []
        for i in range(numero_objetos):
            n.append(sys.stdin.readline().split())
        for j in n:
            if int(j[0]) < 1: precos.append(1)
            elif int(j[0]) > 100: precos.append(100)
            elif int(j[1]) < 1: pesos.append(1)
            elif int(j[1]) > 30:
                pesos.append(30)
            else:
                precos.append(int(j[0]))
                pesos.append(int(j[1]))
        int_grupo = int(input())
        if int_grupo < 1: pesos = 1
        if int_grupo > 100: pesos = 100
        carga_max_por_n = []
        for _ in range(int_grupo):
            c = int(input())
            if c < 1: c = 1
            elif c > 30:
                c = 30
            else:
                carga_max_por_n.append(c)
        print(solve(precos, pesos, carga_max_por_n))
        T -= 1
    #fim = datetime.datetime.now()
    #print(fim - inicio)
