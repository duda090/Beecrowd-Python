investimento_inicial = float(input())
taxa_juros = float(input())
anos = int(input())

taxa_decimal = taxa_juros / 100

valor_final = investimento_inicial * (1 + taxa_decimal) ** anos

print(f"{valor_final:.2f}")