passwd = "FrancoCaudillo"

inp=str(input("Introduce la contraseña: "))
if passwd.lower() == inp.lower():
    print("Contraseña Correcta")
else: 
    print("Contraseña incorrecta")