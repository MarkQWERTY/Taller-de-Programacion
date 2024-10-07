ingresos = float(input("Introduce los ingresos mensuales: "))
puntos=0
if 0 <= ingresos < 1800:
    puntos = 4
elif 1800 <= ingresos < 3500:
    puntos = 3
elif 3500 <= ingresos < 5000:
    puntos = 2
elif ingresos <= 3500:
    puntos = 1

print(f"Puntos: {puntos}")