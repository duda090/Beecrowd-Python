plano = input()
salario = float(input())

if plano == 'A':
    aumento = salario + (salario * 0.10)
    print(f"Novo salário: R${aumento:.2f}")
elif plano == 'B':
    aumento = salario + (salario * 0.15)
    print(f"Novo salário: R${aumento:.2f}")
elif plano == 'C':
    aumento = salario + (salario * 0.20)
    print(f"Novo salário: R${aumento:.2f}")