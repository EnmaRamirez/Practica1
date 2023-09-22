#Taking kilometers input from the user/Tomando kilómetros de entrada de la usuaria.
kilometers = float(input("Enter value in kilometers: "))

#conversion factor/factor de conversión
conv_fac = 0.621371

#calculate miles/calcular millas
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
