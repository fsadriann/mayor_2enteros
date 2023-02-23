# Programa para verificar cuál de dos números enteros es el mayor

#input

print("----------------------------------------------")
print("----- Ingrese los dos enteros a comparar -----")
print("----------------------------------------------")


x = int(input("Digite el valor de x: "))

y = int(input("Digite el valor de y: "))
#processing

if x == y:
    print ("los numeros son iguales ")
else:
    if x > y:
        mayor = x
    else:
        mayor = y
    print("El mayor entre " + str(x) + " y " + str(y) + " es " + str(mayor))