my_list = [1, 2, 3]

# continue
for item in my_list:
    continue  # Salta al siguiente elemento sin ejecutar el código debajo
    print(item)
    continue  # Esto nunca se ejecutará

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 0  # Esto no cambiará el valor de i, provocando un bucle infinito
    continue  # Esta instrucción no tiene efecto aquí

# pass
for item1 in my_list:
    pass  # No hace nada, simplemente pasa al siguiente bloque de código
    print(item1)  # Esto se ejecutará normalmente

while i < len(my_list):
    print(my_list[i])
    i += 1
    pass  # No tiene efecto en este contexto

# break
for item2 in my_list:
    print(item2)
    break  # Sale del bucle después de imprimir el primer elemento

while i < len(my_list):
    print(my_list[i])
    i += 1
    break  # Sale del bucle while después de imprimir el primer elemento
