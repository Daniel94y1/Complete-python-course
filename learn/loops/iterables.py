user ={
    'name':'Golem',
    'age':5006,
    'can_swim':False
}

for key, value in user.items(): #esto de aqui lo relaciona con el user
    print(key, value) # al poner user.items, y luego imprimirlo, imprime todo el contenido de user.

for item in user.values():
    print(item) # al poner user.values, y luego imprimirlo, imprime solo el valor de las variables de user.

for item in user.keys():
    print(item) # al poner user.keys, y luego imprimirlo, imprime solo las variables (sin el valor de estas) de user.

# iterable - list, dicionary, tuple, set, string
# iterated --> one by one check each item in the collection

