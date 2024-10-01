#Quinto ejercicio:

numero = int(input("Introduce el numero de telefono con el prefijo y la extension (+34-numero-extensión): "))   # Le pedimos al usuario el numero con la extension y el +34
numero1 = numero[4:13]      # Reducimos el numero dado quitando asi el +34 y la extensión

print ("El número sin +34 y sin la extensión quedaria tal que asi:",numero1)    # Le damos la solución al usuario que hemos hecho en la linea de arriba