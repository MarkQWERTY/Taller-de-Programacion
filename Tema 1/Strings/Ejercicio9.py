amr=str(input("Introduce una cantidad en formato español: "))

esp = amr.replace(",","A")
otg = esp.replace(".",",")
new = otg.replace("A",".")
print("Cantidad en formato americano: "+new)