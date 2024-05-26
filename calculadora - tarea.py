from funciones_calculadora import *

seguir = "s"
flag_x = False
flag_y = False
flag_calcular = False
x = "-"
y = "-"

while seguir == "s":
  match menu(x, y):
    
    case "1":
      
      if flag_x == False:
        x = float(input("Ingrese el 1er operando: "))
        flag_x = True
      
      elif flag_x == True:
        print("Ya ingresó el 1er operando.")

    case "2":
      
      if flag_y == False:
        y = float(input("Ingrese el 2do operando: "))
        flag_y = True
      
      elif flag_y == True:
        print("Ya ingresó el 2do operando.")

    case "3":
      
      if flag_x == False:
        print("Falta ingresar el 1er operando.")
      
      elif flag_y == False:
        print("Falta ingresar el 2do operando.")
      
      elif flag_calcular == True:
        print("Ya se calcularon las operaciones")

      else:
        resultado_suma = suma(x, y)
        resultado_resta = resta(x, y)
        resultado_multiplicacion = multiplicar(x, y)
        resultado_factorial_a = factorial(x)
        resultado_factorial_b = factorial(y)
        if y == 0:
          print("Todas las operaciones se han calculado exitosamente excepto la división.")
          flag_calcular = True

        else:
          resultado_division = division(x, y)
          print("Todas las operaciones se han calculado exitosamente.")
          flag_calcular = True

    case "4":
      if flag_calcular == False:
        print("Para poder mostrar los resultados, primero debe calcularlos.")
      
      elif flag_calcular == True and y != 0:
        print(f"El resultado de {x} + {y} es {resultado_suma}")
        print(f"El resultado de {x} - {y} es {resultado_resta}")
        print(f"El resultado de {x} * {y} es {resultado_multiplicacion}")
        print(f"El resultado de {x} / {y} es {resultado_division}")
        print(f"El factorial de {x} es {resultado_factorial_a} y el factorial de {y} es {resultado_factorial_b}")
        flag_x = False
        flag_y = False
        flag_calcular = False
        x = "-"
        y = "-"

      elif flag_calcular == True and y == 0:
        print(f"El resultado de {x} + {y} es {resultado_suma}")
        print(f"El resultado de {x} - {y} es {resultado_resta}")
        print(f"El resultado de {x} * {y} es {resultado_multiplicacion}")
        print(f"El factorial de {x} es {resultado_factorial_a} y el factorial de {y} es {resultado_factorial_b}")
        flag_x = False
        flag_y = False
        flag_calcular = False
        x = "-"
        y = "-"
      

    case "5":
      print("Fin del programa")
      break
      

  pausar()