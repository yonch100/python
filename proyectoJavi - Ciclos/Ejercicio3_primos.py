num = 1
while num <= 1:
    num = int(input("Ingrese el número a comprobar: "))

for i in range(2, num):
    if num % i == 0:
        print("Numero no es primo.")
        break
else:
    print("Número primo!")