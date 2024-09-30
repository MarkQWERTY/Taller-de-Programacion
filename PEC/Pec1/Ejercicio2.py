kg = float(input("Introduce tu peso (en kilogramos): "))
altura = float(input("Introduce tu estatura (en metros): "))

imc = kg/altura**2
print("Tu índice de masa corporal (IMC) es de %.2f"%(imc))