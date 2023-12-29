# lists
list=[1,2,3,4,5]
list1=['a','b','c']
list2=[1,2,'a',True]
amazon_cart=['notebooks','sunglasses','toys','grapes']
amazon_cart[0]='laptop'
new_cart=amazon_cart[:] #esto hace que la nueva lista sea una copia de la lista original, asi se soluciona el problema de que si modifico la list original, tambien se modifica la nueva lista
new_cart[0]='gum'
print(new_cart)
print(amazon_cart[0])