ran = int(input("Inserte el rango: "))
mul = int(input("Ingrese numero a comparar: "))
 
for i in range (1, ran + 1):
 if i % mul == 0:
   print(i, "es multiplo de", mul)