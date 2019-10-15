respuesta = " "
cont = 0
while (respuesta != "n"):
 numeropar = int(input ("Ingrese un numero par: "))
 if numeropar % 2 ==0:
     respuesta = str(input("Quiere ingresar otro numero par (s/n): ")).lower()
     cont += 1
 elif numeropar % 2 != 0:
   print(numeropar, "No es un numero par intente nuevamente")
   respuesta = str(input("Quiere ingresar otro numero par (s/n): ")).lower()
 
 
print("Ha escrito", cont,"numeros pares")