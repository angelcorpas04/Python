# El input recoge el dato y lo guarda en nombre.
nombre = input("Introduce tu nombre:")
print ("Hola" + nombre)

# Existen dos tipos de =s en programación:
# = -> Asigna lo que hay a la izquierda a lo que hay a la derecha. Ej. numero = 5
# == -> Es un igual LÓGICO. ¡Compara los valores que tiene a izq y der!
#       Devuelve true, si son iguales; o false, si son distintas.

# 1. Entrada: numero. Salida: True si es mayor de edad.
# Input siempre guarda el valor introducido como str. Si queremos que sea un int hay que transformarlo. int(input)...))
numero = int(input("Introduce tu edad: "))
# Para saber el tipo -> print(type(numero))
print ("¿Es mayor de edad?" )
print (numero >= 18)

# 2. Entrada: dia semana. Salida: True si es fin de semana.
diaSemana = input("¿Qué día de la semana es?: ")
print ("¿Es fin de semana?" )
print (diaSemana == "sabado" or diaSemana == "domingo")

# 3. Entrada: numero. Salida: True si es positivo.
numero = int(input("Introduce un número: "))
print ("¿Es positivo?" )
print (numero >= 0)

# 4. Entrada: letra. Salida: True si es vocal.
letra = input("Introduce una letra: ")
print ("¿Es vocal?" )
print (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u")

# 5. Entrada: numero. Salida: True si está aprobado.
numero = int(input("Introduce tu calificación: "))
print ("¿Está aprobado?" )
print (numero >= 5 and numero <=10)
