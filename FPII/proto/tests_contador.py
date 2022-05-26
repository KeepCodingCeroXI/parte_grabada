from contador import creaContador, Contador

c1 = creaContador()

c2 = creaContador(5)

c3 = Contador()

c4 = Contador(5)
print(c1(), c3.click()) #1
print(c2(), c4.click()) #6

