#Generar una lista a base de los datos entregados


palabras=[]
for i in range (5):
  print ("Ingrese la palabra",i+1)
  palabra=input()
  palabras.append(palabra)

#Ordenar los datos de la lista
def ordenar_por_tamaño(palabras):
  palabras.sort(key=len,reverse=True)

ordenar_por_tamaño(palabras)

#Eleccion de ordenamiento
while True:
  print ("Seleccione una opcion:")
  print ("1. Orden alfabetico")
  print ("2. Orden por tamaño, mayor a menor")
  print ("3. Orden aleatorio")
  print ("4. Orden inverso al ingresado")
  print ("5. Orden igual al ingresado")
  print ("6. Salir")
  seleccion=input()

  match seleccion:
    case "1":
      palabras_ordenadas = sorted(palabras)
    case "2":
      palabras_ordenadas = ordenar_por_tamaño (palabras)
    case "3":
      import random
      random.shuffle(palabras)
      palabras_ordenadas = palabras
    case "4":
      palabras_ordenadas = list(reversed(palabras))
    case "5":
      palabras_ordenadas = palabras
    case "6":
      break
    case _:
      print ("Opcion no valida. Elija una opcion del 1 al 6.")
      continue

#Mostrar ordenamiento elegido
  print ("\nPalabras_ordenadas")
  for palabra in palabras_ordenadas:
    print (palabra)