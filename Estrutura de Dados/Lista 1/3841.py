N = int(input())
numeros = list(map(int, input().split()))
T = int(input())
seen = set()
resultados = []
for num in numeros:
    complemento = T - num
    if complemento in seen:
        resultados.append(tuple(sorted((num, complemento))))
    seen.add(num)
resultados = sorted(set(resultados))
for combinacao in resultados:
    print(combinacao)
