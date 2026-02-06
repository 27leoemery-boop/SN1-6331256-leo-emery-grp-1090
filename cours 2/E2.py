print("pression systolique")
matin = input("Mesure du matin : ")
aprem = input("Mesure du midi :")
soir = input("Mesure du soir :")
moyenne = (float(matin) + float(aprem) + float(soir))/3
print (f"Moyenne de la pression systolique :{moyenne}")