from contador import creaContador, creaContadorReutilizable, Contador

click1 = creaContador()

click2 = creaContador(5)

clickR1 = creaContadorReutilizable()

clickR2 = creaContadorReutilizable(5)

cuentaClicks1 = Contador()

cuentaClicks2 = Contador(5) 

print(click1(), clickR1(consulta=True), cuentaClicks1.consulta(), clickR1(), clickR1(consulta=True), cuentaClicks1.click()) #1

print(click2(), clickR2(consulta=True), clickR2(), clickR2(consulta=True)) #6

clickR1()
clickR1()
clickR1()

print(clickR1(consulta=True)) #4
print(clickR1(reset=0)) #0
print(cuentaClicks1.reset(0))
print(clickR1(consulta=True)) #0
print(clickR1()) #1
