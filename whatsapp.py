import pywhatkit

numero_telefono = input("ingresa numero de telefono: ")
pywhatkit.sendwhatmsg(numero_telefono, "text", 9, 40)