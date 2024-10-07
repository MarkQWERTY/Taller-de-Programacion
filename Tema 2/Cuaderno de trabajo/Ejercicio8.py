def imprimir_monomio(coeficiente, exponente):
    # Caso donde no imprimimos nada si el coeficiente es 0
    if coeficiente == 0:
        return ""
    
    # Para almacenar el resultado del monomio
    resultado = ""
    
    # Determinamos el signo del coeficiente
    if coeficiente > 0:
        resultado += "+"  # Añadimos el signo "+" si el coeficiente es positivo
    
    # Caso cuando el coeficiente es -1 o 1, simplificamos la salida
    if abs(coeficiente) != 1 or exponente == 0:
        resultado += str(coeficiente)  # Imprimimos el coeficiente si no es 1 o -1
    
    # Caso cuando el coeficiente es -1 o 1 y no imprimimos el 1
    if abs(coeficiente) == 1 and exponente > 0:
        if coeficiente == -1:
            resultado += "-"  # Imprimimos solo el "-" si el coeficiente es -1
    
    # Imprimimos la variable 'x' si el exponente es mayor que 0
    if exponente > 0:
        resultado += "x"
    
    # Si el exponente es mayor a 1, lo imprimimos
    if exponente > 1:
        resultado += f"**{exponente}"
    
    return resultado

# Ejemplo de uso
polinomio = [
    (2.0, 3),   # 2.0x**3
    (1, 1),     # x
    (4.0, 0)    # 4.0
]

resultado = "".join([imprimir_monomio(coef, exp) for coef, exp in polinomio])

# Imprimimos el resultado final del polinomio
print(resultado)
