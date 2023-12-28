user ={
    'basket':[1,2,3],
    'greet':'hello',
}

print(user.get('age')) #prints None because there is no key 'age'
print(user.get('age',55)) #prints 55 because there is no key 'age' and the default value is 55
print(user)