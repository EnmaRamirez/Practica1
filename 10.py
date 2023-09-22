#Python program to check if the input number is odd or even./programa ython para verificar si el número ingresado es par o impar.
#A numbers is even if division by 2 gives a remainder of 0./Un número es par si al dividirlo entre 2 el resto es 0.
#If the remainder is 1, it is an odd number./Si el resto es 1, es un número impar.
num = int(input("Enter  Number: "))
if (num% 2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))