nota = float(input("Introduce la calificacion: "))

if 0 < nota < 5:
    print("Suspenso")
elif 5 <= nota <= 6.5:
    print("Aprobado")
elif 6.5 < nota <= 8.5:
    print("Notable")
elif 8.5 <nota<=10:
    print("Sobresaliente") 
