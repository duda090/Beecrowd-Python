num_itens = int(input())

total_compra = 0.0

for i in range(num_itens):
    preco_unitario = float(input())
    quantidade = int(input())
    total_compra += preco_unitario * quantidade

cupom_desconto = float(input())

desconto = (cupom_desconto / 100) * total_compra

valor_final = total_compra - desconto

print(f"Total: R$ {total_compra:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")