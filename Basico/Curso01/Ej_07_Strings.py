#Los strings son un tipo de dato donde se almacena secuencias de
#caracteres alfanumericos y simbolos. Se definen utilizando 
#comillas simples o dobles. 

#Ejemplo , se pide al usuario que ingrese una cadena de texto y se
#muestran diferentes metodos (funciones) para modificar cadenas de
#texto

print('Prueba de metodos de datos string')
str_usuario = input("Ingrese un cadena de texto: ")
print('Tu cadena tiene: ', len(str_usuario), ' caracteres')
print('Tu cadena tiene: ', str_usuario.count('a'), 'letras a')
print('En tu cadena hay solo minusculas?: ',str_usuario.islower())
print('Convierto tu cadena a mayusculas: ', str_usuario.upper())

#tambien se puede dar formato a los string de salida utilizando
#print(f' ') y el operador {}

print("Prueba de formato de la salida utilizando print(f' ')")
str_nombre = input('Ingresar tu nombre: ')
str_apellido = input('Ingresar tu apellido: ')
print(f'Tu nombre completo es: {str_nombre} {str_apellido}')
print('Se puede acceder a cada caracter de un string utilizando []')
print('Los dos primeros caracteres de tu cadena son :')
print(str_nombre[0])
print(str_nombre[1])
