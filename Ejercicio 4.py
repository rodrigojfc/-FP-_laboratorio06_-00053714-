import random
 
x = random.randrange(1,10)
cont=0
y = 0
while x != y:
 y = int(input("Ingrese un numero del 1 al 10: "))
 if y > x:
   print("Ingrese un numero menor")
 elif y < x:
   print("Ingrese un numero mayor")
 cont += 1
print("Felicidades!! Tu numero de intentos fue:", cont)
