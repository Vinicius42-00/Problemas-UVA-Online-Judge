import math
import sys

def get_input_list():
    dim = input()
    M, N, Q = dim.split()
    M = int(M)
    if M > 100: M = 100
    #if M < 1: M = 1
    N = int(N)
    if N > 100: N = 100
    #if N < 1: N = 1
    Q = int(Q)
    mat = []
    intersecs = []
    for i in range(M):
        mat.append(list(sys.stdin.readline().strip()))
    for i in range(Q):
        intersecs.append(list(map(int, list(sys.stdin.readline().split()))))
    return M, N, Q, mat, intersecs

def solve(M,N,mat,intersec):
        a = 1
        elem = mat[intersec[0]][intersec[1]]
        tamanho = 1
        while True:
            if ((intersec[0] - a) < 0) or ((intersec[0] + a) > (M - 1)): break
            if ((intersec[1] - a) < 0) or ((intersec[1] + a) > (N - 1)): break
            for i in range(intersec[0] - a, intersec[0] + a + 1):
                for j in range(intersec[1] - a, intersec[1] + a + 1):
                    #print(f'item:{mat[i][j]}')
                    if mat[i][j] == elem:
                        pass
                    else:
                         return tamanho
            a += 1
            tamanho += 2
        return tamanho

def maior_quadrado_forca_bruta(param):
    M, N, Q, mat, intersecs = param
    resultado = []
    param_str = [str(M), str(N), str(Q)]
    resultado.append(' '.join(param_str))
    for intersec in intersecs:
        resultado.append(str(solve(M,N,mat,intersec)))
    return '\n'.join(resultado)



if __name__ == '__main__':
    T = int(sys.stdin.readline())
    if T > 21: T = 21
    if T < 1: T = 1
    while T > 0:
        print(maior_quadrado_forca_bruta((get_input_list())))
        T -= 1


