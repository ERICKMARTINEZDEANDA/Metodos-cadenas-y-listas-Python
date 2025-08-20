#Metodos de cadenas
#count(“x”,inicio,fin)
#Cuenta las veces que se repite un carácter o una cadena (x) en el rango de inicio a fin
cadena1="La violencia es el ultimo recurso del incompetente"
print(cadena1.count("e"))
cadena1="La violencia es el ultimo recurso del incompetente"
print(cadena1.count("violencia"))


#lower()
#Cambia a minúsculas todos los caracteres de la cadena
print(cadena1.lower())

#upper()
#Cambia a mayúsculas todos los caracteres de la cadena
print(cadena1.upper())

#replace(“x”,“y”,“numero”)
#Remplaza los valores de “x” por “y” de la cadena de acuerdo al número de veces que se especifique.
print (cadena1.replace("recurso","medio",1))

#split(“x”,numero)
#Busca los caracteres iguales a “x”, los quita y organiza nuevas sub-cadenas. Puede modificarse 
#el número de veces que quita los caracteres.
print (cadena1.split("o",2))
print(cadena1)

#find(“x”)
#Busca el caracter “x” de izquierda a derecha y regresa el índice donde se encuentra.
print(cadena1.find("e"))

#rfind("x")
#Busca el caracter “x” de derecha a izquierda y regresa el índice donde se encuentra.
print(cadena1)
print(cadena1.rfind("e"))


#join("x")
#Junta los elementos de una tupla o lista con el elemento “x”.
l1 = ["A","B","R","A","H","A","M"]
v = "-"
print (v.join(l1))	



