#Ejemplo del uso de variables

#las variables no necesitan declararse con un tipo de dato
#específico ni usar palabras reservadas.  

#En Python, declaras una variable usando minúsculas
#y separando las palabras con un guion bajo (_). Esta
#convención se conoce como snake_case. Las variables se crean 
#automáticamente en el momento que les asignas un valor 
#por primera vez utilizando el signo igual (\(=\))

valor_1 = 15
valor_2 = 45
suma = valor_1 + valor_2
print('El resultado es: ', suma)

#Los tipos de variables mas utilizados Enteros, Punto
#flotante, texto, tipo lógico

#ejemplo de concatenación en print
msg_respuesta = 'La respuesta'
print(msg_respuesta,' es', suma + 10)

#tambien se puede cambiar el tipo de variable de un tipo
#a otro (casting), con las funciones integradas int(), 
#float(), str() o bool()

dato_1 = 15.25
dato_2 = 14.85
suma = int(dato_1 + dato_2)
print('La suma en entero es: ', suma)
print('pero la suma en punto flotante es: ',dato_1 + dato_2)




