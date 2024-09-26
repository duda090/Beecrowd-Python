valHora = float(input())
hrsTrab = float(input())

bruto = valHora * hrsTrab

impostoR = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
resul = bruto - (impostoR + inss + sindicato)

print(f"Salário bruto: R${bruto:.2f}")
print(f"Imposto: R${impostoR:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Líquido: R${resul:.2f}")