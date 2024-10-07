a = float(input("Introduce el valor de A: "))
b = float(input("Introduce el valor de B: "))
c = float(input("Introduce el valor de C: "))

try:
    resultA=float((-b+(b**2-4*a*c)**0.5)/(2*a))
    resultB=float((-b-(b**2-4*a*c)**0.5)/(2*a))
except:
    print("El resultado es imaginario")
else:
    print(f"Los resultados son {resultA} y {resultB}")