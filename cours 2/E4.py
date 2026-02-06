import math


print ("point A")
x1= input ("X1 : ")
y2= input ("Y2 : ")

print ("point B")
x3= input ("X3 : ")
y4= input ("Y4 : ")

distance = math.sqrt(((int(x3) - int(x1))**2) + ((int(y4) - int(y2))**2))
print (f"distance : {distance:.2f}")