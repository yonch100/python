nombre = input("Nombre de la persona a donar sangre: ")
sexo = input("Ingresa tu sexo:\nM: Masculono\nF: Femenino\n").upper()
ayunas = (input("¿El donador viene en ayunas?: \nSi: S--- No: N\n")).upper() # no donar en ayudas

edad = float(input("Captura la edad del donador/a: ")) #18 y 65
peso = float(input("Captura el peso del donador/a: ")) #>50 kl
presionArterialdistolica = float(input("Captura la presion arterial D del donador/a: ")) # Tensión diastólica (la baja): entre 50mm Hg y 100 mm Hg ---
presionArterialasistolica = float(input("Captura la presion arterial A del donador/a: "))#Tensión sistólica (la alta): entre 90mm y 180mm Hg
pulso = float(input("Captura el pulso del donador/a: ")) #regular y entre 50 y 110 pulsaciones
plaquetas = float(input("Captura las plaquetas del donador/a: ")) # plaquetas más de 150.000 cc
proteinas = float(input("Captura las proteinas del donador/a: ")) # proteínas totales más de 6 gr/dl (Sólo en donación por aféresis).
# #AGREGAR VALIDACION AFERESIS
hemoglobina = float(input("Captura la hemoglobina del donador/a: ")) # En hombres 13,5 gramos por litro --- en Mujeres superior a 12,5 gramos por litro.

if edad >= 18 and edad <= 65:
    if ayunas == "N":
        if peso >= 50:
            if presionArterialdistolica >= 50 and presionArterialdistolica <= 100 or presionArterialasistolica >= 90 and presionArterialasistolica <= 180:
                if pulso >= 50 and pulso <= 110:
                    if plaquetas > 150.0:
                        if proteinas > 6:
                            if sexo == "F":
                                    if hemoglobina < 12.5:
                                        print("Tus Datos")
                                        print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
                                        print("***No Puedes Donar sangre porque nivel de hemoglobina es menor a 12.5")
                                    else:
                                        print("Gracias por tu donacion")
                            else:
                                    if hemoglobina < 13.5:
                                        print("Tus Datos")
                                        print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
                                        print("***No Puedes Donar sangre porque nivel de hemoglobina es menor a 13.5")
                                    else:
                                        print("Gracias por tu donacion")
                        else:
                            print("Tus Datos")
                            print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
                            print("***No Puedes Donar sangre porque nivel de proteinas es menor a 6")
                    else:
                        print("Tus datos")
                        print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
                        print("***No Puedes Donar sangre porque nivel de plaquetas es inferior a 150.00")
                else:
                    print("Tus datos")
                    print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
                    print("***No Puedes Donar sangra porque tu pulso es menor a 50 o mayor a 100")
            else:
                print("Tus datos")
                print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
                print("***No Puedes Donar sangre porque tu presion arterial esta fuera de los limites")
        else:
            print("Tus datos")
            print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
            print("***No puedes Donar sangre porque tu peso es menor de 50 Kilos")
    else:
        print("Tus datos")
        print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
        print(f"***No Puedes Donar sangra porque tu edad no entra en el rango de 18 y 65 años")
else:
    print("Tus datos")
    print(f"Edad: {edad}\nPeso {peso}\nPresion Arterial D: {presionArterialdistolica}\nPresion Arterial A: {presionArterialasistolica}\nPulso:{pulso}\nPlaquetas: {plaquetas}\nProteinas: {proteinas}")
    print(f"***No Puedes Donar sangra porque tu edad no entra en el rango de 18 y 65 años")
