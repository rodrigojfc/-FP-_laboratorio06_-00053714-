y = int(input("Precio de pelicula 1: "))
x = int(input("Precio de pelicula 2: "))
z = int(input("Precio de pelicula 3: "))
 
precio = 0
 
if y < x and z < x:
 precio = y + z
elif x < y and z < y:
 precio = z + x
elif y < z and x < z:
 precio = x + y
elif x == y and x == z:
 precio = 2*x
elif y == x and z < x:
  precio = z + y
elif y == z and  x < z:
  precio = y + x
elif x == z and y < z:
  precio = x + y
 
print("Su total a pagar es:",precio)