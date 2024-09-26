n = int(input())
primo = True
if n <=1:
    primo = False
else:
    i = 2
    limite = int(n**0.5)
    while i <= limite:
        if n % i == 0:
            primo = False
        i += 1
    if n % i == 0 and n != i:
        primo = False
if primo:
    print("PRIMO")
else:
    print("NÃO PRIMO")