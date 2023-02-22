# Programa para verificar cuál de dos números enteros es el mayor

#input

print("----------------------------------------------")
print("----- Ingrese los dos enteros a comparar -----")
print("----------------------------------------------")


x = int(input("Digite el valor de x: "))

y = int(input("Digite el valor de y: "))
#processing

if x > y:
    msj = " es mayor que "
elif x < y:
    msj = " es menor que "
else:
    msj = " es igual a "

#output

print("El numero " + str(x) + msj + str(y))