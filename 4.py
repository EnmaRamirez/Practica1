#python program to find the area of triangle/programa Python para encontrar el área de un triángulo

a = 5
b = 6
c = 7

#Uncomment below to table inputs from the user/Descomentar a continuación para tabular las entradas del usuario
# a = float(input('enter first side: '))/float(entrada('ingrese el primer lado: '))
# a = float(input('enter second side: '))
# a = float(input('enter third side: '))

#calculate the semi-perimeter/calcular el semiperímetro
s = (a + b + c) / 2

#Calculate the area
area = (s*(s-a)*(s-b)*(s-c))** 0.5
print('The area of the triangle is %0.2f' %area)

