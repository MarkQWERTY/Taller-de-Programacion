edad = int(input("Indique su edad: "))
ingresos = int(input("Introduzca cuales son sus ingresos mensuales: "))

if edad >=16 and ingresos >=1000:
    print("Usted debe pagar el impuesto")
else:
    print("Usted esta exento de pagar el impuesto")