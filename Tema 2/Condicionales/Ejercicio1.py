num=input("Introduce un Número: ")

try:
    x = int(num)
except:
    print("Error: Is not a number")
else:
    if x % 3 ==0:
        print("El número es multiplo de 3")
    else:
        print("El número no es multiplo de 3")