print("-----------------------------------------1")
word = "python"
for i in word:
    print(i)

print("-----------------------------------------2")

for i in word:
    if i == "t":
        break
    print(i)

print("-----------------------------------------3")

# range
# start (opcional) tiene valor por defecto de 0
# stop (obligatorio) siempre llega a 2 menos que este valor
# step (opcional) valor por defecto de 1

for i in range(0,3):
    print(i)

print("-----------------------------------------4")

for i in range(3):
    print(i)

print("-----------------------------------------5")

for i in range(1,6,2):
    print(i)

print("-----------------------------------------6")

for i in range(2,-1,-1):
    print(i)

print("-----------------------------------------7")

for i in range(5,21,3):
    print(i)

print("----------------------------------------TABLA DEL 9")

for i in range(1,10):
    for j in range(1,10):
        result = i*j
        print(f"{i} * {j} = {result}")