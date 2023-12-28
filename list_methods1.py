basket=['a','b','c','d','e']

print(basket.index('d',0,4)) #returns the index of the specified object
print('d'in basket) #returns a boolean value, returns true
print('x'in basket) #returns a boolean value, returns false
print(basket.count('d')) #returns the number of times the specified object appears