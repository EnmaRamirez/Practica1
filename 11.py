#Python program to check if year is a leap year or not/Programa Python para comprobar si el año es bisiesto o no

year = 2023
#To get year (integer input) from the user/Para obtener el año (entrada de entero) de la usuario
#year = int("Enter a year: "))

#Divided by 100 means century year (ending with 00)/Dividido por 100 significa siglo año (que termina en 00
#century year divided by 400 is leap year/El año del siglo dividido por 400 es el año bisiesto.

if (year % 400 ==0) and (year % 100 == 0):
    print("{0}is a leap year". format(year))

    #Not vidive by 100 means not a century year/No dividir por 100 significa que no es un año del siglo. 
    #year divided by 4 is a leap year/el año dividido por 4 es bisiesto
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0}is a leap year". format(year))

    #if not divided by both 400 (century year) and 4 (not century year)/si no se divide por 400 (siglo año) y 4 (no siglo año)
    #year is not leap year/el año no es bisiesto
else:
    print("{0}is a leap year". format(year))

 