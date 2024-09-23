frase="Sherlock Holmes es un detective privado de ficción creado en 1887 por el escritor británico Sir Arthur Conan Doyle."
print("Mayusculas:",frase.upper())
print("Minusculas:",frase.lower())
print("Nº de caracteres:",len(frase))
print(frase.lower().count("a")+frase.lower().count("e")+frase.lower().count("ia")+frase.lower().count("o")+frase.lower().count("u"))
print(len(frase)-(frase.lower().count("a")+frase.lower().count("e")+frase.lower().count("ia")+frase.lower().count("o")+frase.lower().count("u")+frase.count(" ")))
print(frase.replace("a","e"))