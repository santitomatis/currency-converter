valorDolar = 0.004878
valorPeso = 205
print("Quieres convertir pesos a dolares o dolares a pesos? (escribe <pesos a dolares> o <dolares a pesos> (sin <>))")
convertir = input("")

if convertir == "pesos a dolares":
    print("¿Cuantos pesos argentinos tienes?")
    pesos_argentinos = int(input(""))
    dolares = round(pesos_argentinos * valorDolar)
    print("Tienes aproximadamente " + str(dolares) + " dolares")

if convertir == "dolares a pesos":
    print("¿Cuantos dolares tienes?")
    dolares = int(input(""))
    pesos_argentinos = round(dolares * valorPeso)
    print("Tienes aproximadamente " + str(pesos_argentinos) + " pesos")

else:
    print("comando no valido, vuelve a ejecutar el programa y escribe bien")


