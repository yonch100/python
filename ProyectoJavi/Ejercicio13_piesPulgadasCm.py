pies = float(input("CEscriba una cantidad en pies: "))
pulgadas = float(input("Escriba una cantidad en pulgadas: "))

piesACm = pies * 30.48
piesAPulgadas = pulgadas * 2.54

cm = piesACm + piesAPulgadas

print(f"{pies} pies y {pulgadas} pulgadas son {cm} centimetros")