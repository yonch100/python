#Se captura los años, intereses y capital, se convierten en tipo float y asigna los valores a sus variables
años = float(input("Dame los años"))
interes = float(input("Dame el interes a cobrar"))
capital = float(input("Dame el capital"))

#se calcula el valor futuro
valorFuturo = capital * (1+(interes / 100) ) ** años