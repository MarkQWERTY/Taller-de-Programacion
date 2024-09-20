a=float(input("Introduce el lado A: "))
b=float(input("Introduce el lado B: "))
c=float(input("Introduce el lado C: "))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("La area del triangulo es de: %.2f"%(area))