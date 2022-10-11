def showEmployee(nombre, salario = 9000):
    print(f"nombre de empleado: {nombre}\nSalario de empleado: {salario}")

showEmployee("Omar")

nombreEmpleado = input("Dame el nombre del empleado: ")
salarioEmpleado = float(input("Dame el salario del empleado: "))
showEmployee(nombreEmpleado, salarioEmpleado)