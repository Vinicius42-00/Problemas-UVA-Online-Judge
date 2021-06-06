# Para fazer as combinacoes
# https://docs.python.org/3/library/itertools.html
from itertools import product
import sys

def get_input_list():
    qtd_palavras = input()
    palavras = []
    regras = []
    for i in range(1, int(qtd_palavras) + 1): # Assumption: ...words greater than 0
        palavras.append(sys.stdin.readline().strip()) # Strip separa por virgula as palavras.
    qtd_regras = int(sys.stdin.readline())
    #print(qtd_regras)
    for i in range(1, qtd_regras + 1):
        regras.append(sys.stdin.readline().strip())
    return qtd_palavras, palavras, qtd_regras, regras

def solucao(param):
    qtd_palavras, palavras, qtd_regras, regras = param
    #print(palavras)
    #print(palavras)
    numeros = [str(i) for i in range(10)]
    #palavras = palavras
    item = []
    resultado = []
    #print(regras)
    for r in regras:
        for _ in r:
            #print(_)
            if _ == '#':
                item.append(palavras)
            else:
                item.append(numeros)
            #print(item)
        for s in product(*item):
            resultado.append(''.join(s))
    print('--')
    return '\n'.join(resultado)


if __name__ == '__main__':
    while True:
        try:
            #qtd_palavras, palavras, qtd_regras, regras = get_input_list()
            print(solucao(get_input_list()))
            #print(palavras)
            #print(qtd_regras)
            #print(regras)
        except Exception: break


