anoAtual = int(input())
salarioInicial = 1000.00
aumento = 0.015
salario = salarioInicial
ano = 2006
if anoAtual < 2006:
    print("O ano informado deverá ser > 2005!")
else:
    while ano <= anoAtual:
        if ano > 2006:
            aumento += 0.01
        salario += salario * aumento
        ano += 1
    print(f"Salário atual: R${salario:.2f}")