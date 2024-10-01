#Cuarto ejercicio: 

ppayasos = 112      # Indicamos el peso de los payasos
pmuñecas = 75       # Indicamos el peso de las muñecas

payasos = int(input("Indica cuantos payasos se han vendido: "))         # Indicamos el numero de payasos que se han vendido por medio del usuario 
muñecas = int(input("Indica cuantas muñecas se han vendido: "))         # Indicamos el numero de muñecas que se han vendido por medio del usuario 

totalp = payasos * ppayasos     # Se calcula la multiplicación del numero de payasos por su peso
totalm = muñecas * pmuñecas     # Se calcula la multiplicación del numero de muñecas por su peso

total = totalm + totalp # Sumamos ambos pesos totales 

print ("El total de payasos vendidos ha sido",payasos,",el total de muñecas vendidas ha sido",muñecas,", por lo tanto el paquete tendra un peso de",total,"gramos")     # Imprimios la cantidad de payasos y muñecas y su peso total