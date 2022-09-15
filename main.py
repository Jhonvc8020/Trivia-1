# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre computación")
print ("Pondremos a prueba tus conocimientos")

# Es importante dar instrucciones sobre cómo jugar:
print ("Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿En que año Brasil gano su ultima copa del mundo?")
print ("a) 1998")
print ("b) 2002")
print ("c) 2014")
print ("d) 2018")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
Mundial = int (input("Digite el año: "))
if Mundial == 2002:
  print("Su respuesta es correcta \n")
else:
  print ("Su respuesta es incorrecta \n")
  

print ("1) ¿En que año se proclamo la independencia del Peru?")
print ("a) 1821")
print ("b) 1815")
print ("c) 1840")
print ("d) 1620")

Independencia= int (input("Digite el año: "))
if Independencia == 1821:
  print("Su respuesta es correcta \n")
else:
  print("Su respuesta es incorrecta \n")

print ("1) ¿En que año Peru fue a su ultima copa del mundo?")
print ("a) 2014")
print ("b) 2018")
print ("c) 2006")
print ("d) 2002")

Pais= int (input("Digite el año: "))
if Pais==2018:
  print ("Su respuesta es correcta \n")
else:
  print("Su repuesta es incorrecta \n")