#python program to find the largest number among the three input numbers

#change the values of num1. num2 and num3
#for a different result
num1 = 10
num2 = 15
num3 = 12

#uncomment following lines to take three numbers from user 
#num1 = floant(input)("Enter first number: "))
#num2 = floant(input)("Enter second number: "))
#num3 = floant(input)("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1)and (num2 >= num3):
    largest = num2
else:
    largest = num3
    print("The largest number is", largest)
