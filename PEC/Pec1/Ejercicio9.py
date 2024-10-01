#Noveno ejercicio: 

tweet = str(input("Introduce el tweet al que quieras contar los #: "))  # Le pedimos al usuario que introduzca el tweet que quiera
hastag = tweet.count("#")                                               # Hallamos los # que tiene el mismo

print ("El numero de hastags en el tweet son ",hastag)                  # imprimimos los resultados