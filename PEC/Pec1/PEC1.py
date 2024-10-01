#Primer ejercicio:
horas = int(input("Dime las horas en formato 24 horas: "))  # Damos las horas que queramos
minutos = int(input("Dime los minutos: ")) # Damos los minutos que queramos
segundos = int(input("Dime los segundos: ")) # Damos los segundos que queramos
horas2 = horas*3600 # Pasamos las horas a segundos 
minutos2 = minutos*60 # Pasamos los minutos a segundos
sect = horas2+minutos2+segundos # Sumamos todo en segundos
sect2 = 86400-sect # Restamos las 24H a los segundos totales 
print ("El total de segundos pasados desde la ultima medianoche son: ",sect) # Imprimimos las soluciones
print ("El total de segundos que quedan para la siguiente medianoche son: ",sect2) # Imprimimos las soluciones
#Segundo ejercicio
peso = float(input("Cual es tu peso en kilogramos: ")) # Indicamos el peso
estatura = float(input("Indica cual es tu estatura en metros: "))# Indicamos la estatura
imc = (peso/(estatura ** 2)) # Implementamos la formula del Indice de masa corporal
imcr = (round (imc, 2)) # Antes de hacer la impresión hacemos el redondeo
print ("Tu indice de masa copropral es:", imcr, "kg/m2") # Finalmente imprimimos la expresión
#Tercer ejercicio
n = int(input("Escriba el numero que quiera: ")) # Se explica al usuario a poner el numero que quiera
if n>= 0: # Como el ejercicio mos explica que tiene que ser positivo se pone una variable para que establezca un numero positivo
    suma =(n*(n+1))/2 # Al ser positivo se hace la formula 
    print ("La suma desde el 1 hasta el numero establecido es: ", suma) #Se imprime la suma
else: # Si el numero no es positivo se le indica al usuario y se acaba el programa
    print("No es un numero positivo") # Se indica que a elegido un numero no positivo
#Cuarto ejercicio
ppayasos = 112 # Indicamos el peso de los payasos
pmuñecas = 75 # Indicamos el peso de las muñecas
payasos = int(input("Indica cuantos payasos se han vendido: ")) # Indicamos el numero de payasos que se han vendido por medio del usuario 
muñecas = int(input("Indica cuantas muñecas se han vendido: "))  # Indicamos el numero de muñecas que se han vendido por medio del usuario 
totalp = payasos * ppayasos # Se calcula la multiplicación del numero de payasos por su peso
totalm = muñecas * pmuñecas # Se calcula la multiplicación del numero de muñecas por su peso
total = totalm + totalp # Sumamos ambos pesos totales 
print ("El total de payasos vendidos ha sido",payasos,",el total de muñecas vendidas ha sido",muñecas,", por lo tanto el paquete tendra un peso de",total,"gramos") # Imprimios la cantidad de payasos y muñecas y su peso total
#Quinto ejercicio
numero = int(input("Introduce el numero de telefono con el prefijo y la extension (+34-numero-extensión): ")) # Le pedimos al usuario el numero con la extension y el +34
numero1 = numero[4:13] # Reducimos el numero dado quitando asi el +34 y la extensión
print ("El número sin +34 y sin la extensión quedaria tal que asi:",numero1) # Le damos la solución al usuario que hemos hecho en la linea de arriba
#Sexto ejercicio
frase = str(input("Introduce la frase que quieras: ")) # Le pedimos al usuario la frase que quiera
vocal = str(input("Introduce la vocal que quieras transformar a mayusucla: ")) # Le pedimos al usuario la vocal que quiera
vocalm = (vocal.upper()) # Transformamos la vocal dada a mayuscula
frasem = frase.replace (vocal, vocalm) # Remplazamos la vocal ya en mayuscula en la frase
print("La frase modificando la vocal que has dado quedaria asi: ", frasem) # Imprimimos la frase ya con la mayuscula
#Septimo ejercicio
nombre = str(input("Introduce tu nombre: ")) # Le pedimos al usuario que nos de un nombre
nombrem = (nombre.upper()) # Transformamos el nombre a mayusculas
numero = (len(nombre)) # Hacemos esta funcion para que nos de el numero de letras que tiene el nombre
print ("El nombre en mayusculas es:",nombrem,"y tiene",numero,"de letras") # Finalmente imprimimos la frase querida
#Octavo ejercicio
frase = str(input("Instroduzca la frase que quieras para invertirla: ")) # Le pedimos al usuario que nos de una frase 
frasei = (frase [::-1]) # Con esta funcion invertimos la frase 
print ("La frase invertida quedaria tal que asi:",frasei) # Para finalizar, imprimos la frase invertida 
#Noveno ejercicio
tweet = str(input("Introduce el tweet al que quieras contar los #: ")) # Le pedimos al usuario que introduzca el tweet que quiera
hastag = tweet.count("#") # Hallamos los # que tiene el mismo
print ("El numero de hastags en el tweet son ",hastag) # imprimimos los resultados

