#Segundo ejercicio:

peso = float(input("Cual es tu peso en kilogramos: "))                  # Indicamos el peso
estatura = float(input("Indica cual es tu estatura en metros: "))       # Indicamos la estatura

imc = (peso/(estatura ** 2))           # Implementamos la formula del Indice de masa corporal
imcr = (round (imc, 2))                # Antes de hacer la impresión hacemos el redondeo

print ("Tu indice de masa copropral es:", imcr, "kg/m2")        # Finalmente imprimimos la expresión