# Program to check if a number is prime or not/Programa para comprobar si un número es primo o no

num = 29

#To take input from the user/Tomar aportes de la usuaria.
#num = int(input("Enter a number: "))/num = int(input("Ingrese un número: "))

#define a flag variable/definir una variable de bandera
flag = False

#prime numbers are greater than 1/los numeros primos son mayores que 1
if num > 1:
    #Check for factors/comprobar los factores
    for i in range(2, num):
        if (num % i) == 0:
        #if factor is found, set flag to True/si se encuentra el factor, establezca el indicador en Verdadero
         flag = True
        #break out of loop/salir del bucle
        break

#check if flag is True/comprobar si la bandera es verdadera
if flag:
    print(num,"is not a prime number")
else:
    print(num, "is a prime number")