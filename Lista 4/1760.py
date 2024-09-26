totalPessoas = 4
acima = 0
somaIdade = 0.0
pessoascadastradas = 0
while pessoascadastradas < totalPessoas:
    idade = int(input())
    peso = float(input())
    if peso > 90:
        acima += 1
    somaIdade += idade
    pessoascadastradas += 1
media = somaIdade / totalPessoas
print(f"Qtd pessoas > 90 Kg: {acima}")
print(f"Idade média: {media:.2f}")