def soma_matrizes():
    m, n = map(int, input().strip().split())
    elementos_a = list(map(int, input().strip().split()))
    elementos_b = list(map(int, input().strip().split()))
    matriz_a = []
    matriz_b = []
    for i in range(m):
        linha_a = elementos_a[i * n:(i + 1) * n]
        matriz_a.append(linha_a)
    for i in range(m):
        linha_b = elementos_b[i * n:(i + 1) * n]
        matriz_b.append(linha_b)
    matriz_resultante = []
    for i in range(m):
        linha_resultante = []
        for j in range(n):
            soma = matriz_a[i][j] + matriz_b[i][j]
            linha_resultante.append(soma)
        matriz_resultante.append(linha_resultante)
    for linha in matriz_resultante:
        print(linha)
soma_matrizes()
