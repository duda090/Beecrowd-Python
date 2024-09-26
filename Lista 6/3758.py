def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def calcular_mmc(a, b):
    mdc = calcular_mdc(a, b)
    return (a * b) // mdc
a = int(input())
b = int(input())
resultado = calcular_mmc(a, b)
print(resultado)