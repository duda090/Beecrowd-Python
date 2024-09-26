codigoCliente = int(input())
valorCompra = float(input())
if codigoCliente ==1:
    print(f"Valor total a ser pago: R${valorCompra:.2f}")
    
elif codigoCliente ==2:
    valPagar = valorCompra - (valorCompra * 0.13)
    print(f"Valor total a ser pago: R${valPagar:.2f}")
elif codigoCliente ==3:
    valPagar = valorCompra - (valorCompra * 0.07)
    print(f"Valor total a ser pago: R${valPagar:.2f}")
    
else:
    print("OPÇÃO INVÁLIDA!")