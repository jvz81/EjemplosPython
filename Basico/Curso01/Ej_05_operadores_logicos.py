#Los operadores logicos permiten combinar y evaluar 
#multiples condiciones (and, or, not)
#estos operados cumplen las tablas de verdad de la logica

#tabla de verdad AND
print('tabla de verdad AND')
print('Solo es verdadero cuando las 2 condiciones son verdaderas')
print('|\tA\t|\tB\t|\tX\t|')
print('|   False\t|   False\t|   ',False and False,'\t|')
print('|   False\t|   True\t|   ',False and True,'\t|')
print('|   True\t|   False\t|   ',True and False,'\t|')
print('|   True\t|   True\t|   ',True and True,'\t|')

#tabla de verdad OR
print('=======================================')
print('tabla de verdad OR')
print('Solo es falso cuando las 2 condiciones son falsas')
print('|\tA\t|\tB\t|\tX\t|')
print('|   False\t|   False\t|   ',False or False,'\t|')
print('|   False\t|   True\t|   ',False or True,'\t|')
print('|   True\t|   False\t|   ',True or False,'\t|')
print('|   True\t|   True\t|   ',True or True,'\t|')

#tabla de verdad NOT
print('=======================================')
print('tabla de verdad NOT')
print('invierte o niega el valor booleano ')
print('|\tA\t|\tX\t|')
print('|   False\t|   ',not False ,'\t|')
print('|   True\t|   ', not True,'\t|')

