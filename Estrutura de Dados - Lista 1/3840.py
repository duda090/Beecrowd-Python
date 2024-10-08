N = int(input())
numeros = list(map(int, input().split()))
maior = numeros[0]
menor = numeros[0]
print(f"Número considerado maior: {maior}")
for num in numeros[1:]:
    if num > maior:
        print(f"Número considerado maior: {num}")
        maior = num
    if num < menor:
        menor = num
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")