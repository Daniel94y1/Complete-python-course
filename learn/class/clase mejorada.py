#00P
class PlayerCharacter:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def run(self):
        print('run')

people= []

while True:
    name= input('Ingrese el nombre del jugador: ')

    if name.lower()=='stop':
        break

    try:
        age= int(input('Ingrese la edad del jugador: '))
    except ValueError:
        print('Por favor ingrese una edad valida')
        continue

    player=PlayerCharacter(name, age)
    people.append(player)

print("{:<15} {:<5}".format("Nombre", "Edad"))
print("-" * 20)

for player in people:
    print("{:<15} {:<5}".format(player.name, player.age))