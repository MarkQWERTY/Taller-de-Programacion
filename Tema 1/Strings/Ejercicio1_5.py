nombre = str(input("Introduzca su nombre: "))
primer_apellido = str(input("Introduzca su primer apellido: "))
segundo_apellido = str(input("Introduzca su segundo apellido: "))

print("Su nombre completo es: " + nombre + " " + primer_apellido + " " + segundo_apellido)
print("Len1:", len(nombre),"Len2:", len(primer_apellido),"Len3:", len(segundo_apellido),"Total:", len(nombre+primer_apellido+segundo_apellido))