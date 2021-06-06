import math
import datetime
import sys
from itertools import accumulate

def get_input_list():
    integer_t = int(sys.stdin.readline())
    # tratando os limites estabelecidos no problema
    #if integer_t < 1: integer_t = 1
    #if integer_t > 25: integer_t = 25
    linhas_teste = int(sys.stdin.readline())
    posicao_i = int(sys.stdin.readline())
    if posicao_i < 1: posicao_i = 1
    if posicao_i > 2147483647: posicao_i = 2147483647
    return [integer_t, linhas_teste, posicao_i]

def sequencia(n):
    seq = []
    s = 0
    for i in range(1, n + 1):
        s = s*10+i
        num = list(str(s))
        for _ in num:
            seq.append(str(_))
    return seq[:n]

def valor_seq(s):
    b = []
    for _ in s:
        b.append(int(_))
    return sum(b)

def lista_val_linhas_sk(linhas):
    list_valores_linhas_sk = []
    for i in range(0, linhas+1):
        list_valores_linhas_sk.append(valor_seq(sequencia(i)))
    return list_valores_linhas_sk

def tam_linhas_sk(linhas_teste):
    tamanho_linhas_sk = []
    for i in range(0, linhas_teste+1):
        tamanho_linhas_sk.append(len(sequencia(i)))
    return tamanho_linhas_sk

def busca_iesimo_posicao(posicao, inicio, fim, seq):
    for _ in seq[inicio:meio]:
        if _ == posicao:
            return sequencia(_)[-1]

def solve(posicao, linhas_teste):
    if linhas_teste > sys.maxsize: linhas_teste = sys.maxsize
    if linhas_teste < 1 : linhas_teste = 1
    i_esimo = None
    #resultado = [str(integer_t)]
    linhas_tam = tam_linhas_sk(linhas_teste)
    #t = integer_t
    #print(t)
    inicio = 0
    fim = len(linhas_tam)
    while inicio < fim:
        meio = (fim + inicio)//2
        #print('loop')
        for _ in linhas_tam[inicio:meio]:
            if _ == posicao:
                i_esimo = sequencia(_)[-1]
            else:
                for _ in linhas_tam[meio+1:fim]:
                    if _ == posicao:
                        i_esimo = sequencia(_)[-1]
        inicio += 1
    return i_esimo


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    resultado = [T]
    for _ in range(T-1):
        linhas_teste = int(input())
        posicao_i = int(input())
        resultado.append(solve(posicao_i, linhas_teste))
    print('\n'.join(list(map(str, resultado))))
