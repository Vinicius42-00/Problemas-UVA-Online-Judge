# Coin Collector

def get_input_list():
    tipos_moedas = int(input())
    valores = []
    valores.append(list(map(int, input().split())))
    return tipos_moedas, valores[0]


def solve(tipos, valores):
    n = len(valores)
    soma = 0
    cont = 0
    ultimo = 0
    for i in range(0, tipos):
        # critério guloso
        if soma >= valores[i]:
            soma = soma - ultimo + valores[i]
        else:
            soma += valores[i]
            cont+=1
        ultimo = valores[i]
    return cont


if __name__ == '__main__':
    T = int(input())
    if T < 1: T = 1
    if T > 1000: T = 1000
    while T:
        tipos_moedas = int(input())
        valores = list(map(int, input().split()))
        print(solve(tipos_moedas, valores))
        T-=1


