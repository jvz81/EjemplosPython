#Para solicitar datos al usuario se utiliza la funcion input()
#esta funcion permite guardar la informacion que ingresa el 
#usuario en una variable, y tambien permite mostrar un mensaje
#de texto para solicitar la informacion al usuario, cuando 
#se utiliza input el programa se detiene hasta que se presiona
#enter

str_nombre = input('Ingrese su nombre: ')
str_apellido = input('Ingrese su apellido: ')
print('Su nombre completo es: ',str_nombre + ' '+ str_apellido)

#Cuando se solicitan numeros, estos se guardan como texto,
#por tanto se tiene que usar int() o float(), para que se
#pueda realizar operaciones con estos

print('Calculo del area del rectangulo')
base = input('Ingrese la base del rectangulo: ')
altura = input('Ingrese la altura del rectangulo: ')
print('El area del rectangulo es: ', int(base)* int(altura))

#Otra forma de ingresar numeros

print('Calculo del area del triangulo')
base = float(input('Ingrese la base del triangulo: '))
altura = float(input('Ingrese la altura del triangulo: '))
print('El area del rectangulo es: ', base*(altura/2))

