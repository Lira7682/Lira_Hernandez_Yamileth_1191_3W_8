print (" ") #espacio a agregar
print ("Lira Hernandez Dayana Yamileth: determina el factorial del valor ingresado")
print (" ") #espacio a agregar

#producto de todos los enteros positivos menores o iguales a n
def factorial(n):
    if n == 0 or n == 1: #Calcula el factorial de un número entero no negativo
       return 1
    else:
       return n * factorial(n - 1)#función que calcula el factorial de un número

n = int(input("Ingrese un numero entero")) #solicita al usuario que ingrese un valor 

if n < 0:
    print("El factorial no está definido para números negativos.")#imprime si el numero es negativo
else:
    print(f"El factorial de {n} es {factorial(n)}.")#imprime el factorial del valor 
print (" ") #espacio a agregar