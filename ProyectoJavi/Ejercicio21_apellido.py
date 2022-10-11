
# write a program that takes your full name as input and displays the abbreviations of the first and
# middle names except the last name whitch is displayed as it is.
# for example, if yoy name is Robert Brett Roser, then the output should be R.B.Roser

fullName = input("Ingresa tu nombre: ").split(" ")

nombre = fullName[0]
nombre2 = fullName[1]
apellido = fullName[2]

print(f"Tu nombre es:  + {nombre[:1].capitalize()}.{nombre2[:1].capitalize()}.{apellido.title()}")