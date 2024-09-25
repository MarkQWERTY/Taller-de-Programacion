adn = "AAGCATCGTGTCATGCATCG"
C=adn.count("GC")
GC=(C*100)/len(adn)
print("El porcentaje de GC es de %.0f"%(int(GC)), "%")
