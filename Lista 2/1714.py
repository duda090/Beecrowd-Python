valProduto = float(input())
if valProduto < 20.00:
    lucro = 0.45
else:
    lucro = 0.30
valorLucro = valProduto * (1 + lucro)
print(f"Valor de venda: R${valorLucro:.2f}")