is_old=bool('hello')
is_licenced=bool(5)

print(bool('hello'))
print(bool(5))

#Truthy vs Falsy

if is_old and is_licenced:
    print('you are old enough to drive!, amd you have a licence')
else:
    print('you are not of age')

print('okoko')