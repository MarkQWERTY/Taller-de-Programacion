a = float(input("Introduce x^2: "))
b = float(input("Introduce x: "))
c = float(input("Introduce número: "))

resultado1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
resultado2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

print("Los resultados son %.2f"%(resultado1),"y %.2f"%(resultado2))
