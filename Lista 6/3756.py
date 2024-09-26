def calcular_fatorial(n):
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial
numero = int(input())
if numero < 0:
    print()
else:
    resultado = calcular_fatorial(numero)
    print(resultado)