import os

def menu(x:str, y:str)->str:
  """
  Imprime el menú en pantalla

  Args:
      x (str): un str que luego será convertido a entero cuando le pasemos el 1er operando
      y (str): un str que luego será convertido a entero cuando le pasemos el 2do operando

  Returns:
      input: para seleccionar la opción que querramos
  """
  
  limpiar_terminal()
  print(f"{'Menú de opciones':^50}")
  print(f"1 - Ingrese 1er operando (A = {x})")
  print(f"2 - Ingrese 2do operando (B = {y})")
  print("3 - Calcular operaciones")
  print("4 - Mostrar resultado")
  print("5 - Salir")

  return input("Ingrese opción: ")

def suma(a:float, b:float)->float:
  """
  Suma dos números

  Args:
      x (float): primer número a sumar
      y (float): 2do número a sumar

  Returns:
      float: el producto de la suma
  """

  suma = a + b
  return suma

def resta(a:float, b:float)->float:
  """
  Resta dos números

  Args:
      x (float): primer número a restar
      y (float): 2do número a restar

  Returns:
      float: el producto de la resta
  """

  resta = a - b
  return resta

def multiplicar(a:float, b:float)->float:
  """
  Multiplica dos números

  Args:
      x (float): primer número a multiplicar
      y (float): 2do número a multiplicar

  Returns:
      float: el producto de la multiplicación
  """

  producto = a * b
  return producto

def division(a:float, b:float)->float:
  """
  Divide dos números

  Args:
      x (float): primer número a divide
      y (float): 2do número a divide

  Returns:
      float: el cociente de la división
  """

  cociente = a / b
  return cociente

def factorial(n:float)->float:
  """
  Calcula el factorial de un número

  Args:
      n (float): número del cual se calcula el factorial

  Returns:
      float: el factorial
  """

  if n == 0:
        return 1
  else:
        return n * factorial(n-1) #Si n es diferente de 0, entonces se utiliza la recursión.
                                  #La función se llama a sí misma con el argumento (n-1) y multiplica el resultado por n. 
                                  #Esto se repite hasta que n llegue a 0, momento en el que se alcanza el caso base y la recursión termina

def limpiar_terminal():
   """
   Limpia la terminal
   """
   os.system("cls")

def pausar():
  """
  Pone en pausa a la terminal
  """
  os.system("pause")

