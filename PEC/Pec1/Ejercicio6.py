#Sexto ejercicio:

frase = str(input("Introduce la frase que quieras: "))                          # Le pedimos al usuario la frase que quiera
vocal = str(input("Introduce la vocal que quieras transformar a mayusucla: "))  # Le pedimos al usuario la vocal que quiera

vocalm = (vocal.upper())                # Transformamos la vocal dada a mayuscula
frasem = frase.replace (vocal, vocalm)  # Remplazamos la vocal ya en mayuscula en la frase

print("La frase modificando la vocal que has dado quedaria asi: ", frasem)  # Imprimimos la frase ya con la mayuscula