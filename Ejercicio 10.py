def far_to_cel():
  a=float(input("Temperatura en Fahrenheit: "))
  b=round(((a-32)*(5/9)),2)
  print(str(a) + "° Fahrenheit = "+str(b)+ "° Celsius")

def cel_to_far():
  a=float(input("Temperatura en Celsius: "))
  b= round((a*(9/5) + 32),2)
  print(str(a) + "° Celsius = " +str(b)+ "° Fahrenheit")

def kel_to_cel(): 
  a=float(input("Temperatura en Kelvin: "))
  b=round((a-273.15),2)
  print(str(a) + "° Kelvin = " + str(b) + "° Celsius")

n=0
while n != 4:
  print("1.- Fahrenheit a Celsius")
  print("2.- Celsius a Fahrenheit")
  print("3.- Kelvin a Celsius")
  print("4.- Salir")
  n=int(input("Elegir una conversion "))
  if n == 1:
    print("Fahrenheit a Celsius")
    far_to_cel()

  elif n == 2:
    print("Celsius a Fahrenheit")
    cel_to_far()

  elif n == 3:
    print("Kelvin a Celsius")
    kel_to_cel()

  elif n != 4:
    print("Elegir una opcion del 1 al 4")

print("Salir")