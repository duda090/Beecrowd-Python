n = int(input())
soma = 0
i = 1
while i <= n:
    if i % 2 == 0:
        soma += i
    i += 1
print(soma)