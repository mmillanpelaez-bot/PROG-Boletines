# 1.
print("Ejercicio 1")
#Vendas anuais			Artigo de consumo
#baixo <= 100 produtos
#>100 e < = 500			medio
#> 500 e < = 1000			alto
#> 1000 				primeira necesidade

# 2.
print("Ejercicio 2")
def area_calculator():
    from math import pi
    while True:
    #print table
        print("-----------------------")
        print ("--Calculador de Areas--")
        print("-----------------------")
        print("-----1. Rectangulo-----")
        print("-----2. Triángulo------")
        print("-----3. Círculo--------")
        print("-----4. Salir----------")
        print("-----------------------")
    #ask input
        option = input("Selecciona un número: ")
    #rectangle
        if option == "1":
            length_str = input("Escribe el largo del rectángulo: ")
            width_str = input("Escribe el ancho del rectángulo: ")
            lenght = float(length_str)
            width = float(width_str)
            area = lenght*width
            print("El area del rectángulo es:", area)
    #triangle
        elif option == "2":
            base_str = input("Escribe la base del triángulo: ")
            height_str = input("Escribe la altura del triángulo: ")
            base = float(base_str)
            height = float(height_str)
            area = base*height
            print("El area del triángulo es:", area)
    #circle
        elif option == "3":
            radius_str = input("Escribe el radio del círculo: ")
            radius = float(radius_str)
            area = pi*radius**2
            print("El area del círculo es:", area)
    #break option
        elif option == "4":
            print("¡Hasta la vista!")
            break
    #else print error
        else: print("Error: Por favor elija un valor correcto.")
area_calculator()