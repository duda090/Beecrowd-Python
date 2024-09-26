nome = input()
hrsExtras = float(input())
salarioMinimo = 1192.40
valorHrExtra = 10.00
salarioHrExtra = hrsExtras * valorHrExtra
salarioBruto = 3 * salarioMinimo + salarioHrExtra
descontoINSS = 0.12 * salarioBruto if salarioBruto > 2000.00 else descontoINSS = 0.5
descontoImpostoR = 0.20 * salarioBruto if salarioBruto > 2500.00 else descontoImpostoR = 0
salarioLiquido = salarioBruto - (descontoImpostoR + descontoINSS)
print("Nome: %s"%(nome))
print(f"Salário bruto: R${salarioBruto:.2f}\nSalário líquido: R${salarioLiquido:.2f}")