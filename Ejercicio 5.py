saldo = 1000
respuesta = str(input("Que desea hacer: Retirar/Depositar: ")).lower()
 
if respuesta == "retirar":
 x = int(input("Cuanto desea retirar: $"))
 if(saldo < x):
   print("El saldo no alcanza para retirar esa cantidad de dinero")
   print("Saldo actual: ", saldo)
 else:
   saldo -= x
   print("Su nuevo balance es: $", saldo)
elif respuesta == "depositar":
 x = int(input("Cuanto desea depositar: $"))
 saldo += x
 print("Su nuevo balance balance es: $", saldo)
else:
 print("No se entiende la selección")