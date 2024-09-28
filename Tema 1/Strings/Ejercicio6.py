cadena1=str(input("Introduzca la primera cadena: "))
cadena2=str(input("Introduzca la segunda cadena: "))

newcad1 = cadena1.replace(cadena1[0:1], cadena2[0:1])
newcad2 = cadena2.replace(cadena2[0:1], cadena1[0:1])

print(newcad1+" , "+newcad2)