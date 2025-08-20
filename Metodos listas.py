#index
#Busca el índice de “x” en la lista; si no se encuentra, marca un error
pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]
print ("index",l1.index("variable"))

#append(x)
#Agrega el elemento “x” a la lista a partir del último valor.
l1.append("constante")
#no se puede print(l1.append("constante"))
print("append", l1)

#count(x)
#Cuenta el número de veces que apareceel valor “x”
print("count",l1.count("constante"))

#insert(índice,x)
#Inserta el valor “x” en el índice que elijas y recorre los demás valores de la lista.
l1.insert(1,"valor nuevo")
print("insert",l1)

#extend(X)
#Agrega una nueva lista, tupla o cadena a otra lista.
l2=["Cesar","Mario","Octavio"]
l1.extend(l2)
print("extend",l1)

#pop(índice)
#Elimina el valor de la lista de acuerdo al índice que elijas.
l1.pop(3)
print("pop",l1)

#remove
#Elimina el primer valor “x” de la lista.
l1.remove("Cesar")
print("remove",l1)

#reverse()
#Invierte el orden de los valores de la lista.
l1.reverse()
print("reverse",l1)



