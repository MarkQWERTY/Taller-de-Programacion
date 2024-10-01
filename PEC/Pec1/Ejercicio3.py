#Tercer ejercicio:

n = int(input("Escriba el numero que quiera: "))        # Se explica al usuario a poner el numero que quiera

if n>= 0:               # Como el ejercicio mos explica que tiene que ser positivo se pone una variable para que establezca un numero positivo
    suma =(n*(n+1))/2   # Al ser positivo se hace la formula 
    print ("La suma desde el 1 hasta el numero establecido es: ", suma)     #Se imprime la suma
else:                   # Si el numero no es positivo se le indica al usuario y se acaba el programa
    print("No es un numero positivo")   # Se indica que a elegido un numero no positivo