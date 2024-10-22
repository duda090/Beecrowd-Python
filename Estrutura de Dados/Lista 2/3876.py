def encontre_elemento(matriz, valor):
    posicoes = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                posicoes.append((i + 1, j + 1))
    if posicoes:
        return posicoes
    else:
        return [(-1, -1)]
def main():
    n, m = map(int, input().strip().split())
    matriz = []
    for _ in range(n):
        linha = list(map(int, input().strip().split()))
        matriz.append(linha)
    valor = int(input().strip())
    resultado = encontre_elemento(matriz, valor)
    for linha, coluna in resultado:
        print(linha, coluna)
main()
