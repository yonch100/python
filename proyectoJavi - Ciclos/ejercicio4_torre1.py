# range
# start (opcional) tiene valor por defecto de 0
# stop (obligatorio) siempre llega a 2 menos que este valor
# step (opcional) valor por defecto de 1

for i in range(1,10):
    # se multiplica el string, en python si se puede
    num = int("1" * i)

    resultado = num * num
    print(f"{num} x {num} = {resultado}")
