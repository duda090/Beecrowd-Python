nivel = int(input())
qtdHoraAula = float(input())
salario = 0
if nivel == 1:
    salario = qtdHoraAula * 12.00
    print(f"Seu salário é de R${salario:.2f}")
elif nivel == 2:
    salario = qtdHoraAula * 17.00
    print(f"Seu salário é de R${salario:.2f}")
elif nivel == 3:
    salario = qtdHoraAula * 25.00
    print(f"Seu salário é de R${salario:.2f}")
else:
    print("O nível digitado não é válido!")