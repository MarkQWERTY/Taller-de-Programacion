letra = str(input("Introduce letra: "))
#Parte 1
if letra.lower().count("a") > 0:
    print("Es vocal")
elif letra.lower().count("e") > 0:
    print("Es vocal")
elif letra.lower().count("i") > 0:
    print("Es vocal")
elif letra.lower().count("o") > 0:
    print("Es vocal")
elif letra.lower().count("u") > 0:
    print("Es vocal")
else:
    print("Es consonante")

#Parte 2

    if letra.lower().count("a") > 0 or letra.lower().count("e") > 0 or letra.lower().count("o") > 0 or letra.lower().count("i") > 0 or letra.lower().count("u") > 0:
        print("Es vocal")
    else:
        print("Es consonante")

