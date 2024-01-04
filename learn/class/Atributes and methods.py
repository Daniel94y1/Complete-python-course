#00P
class PlayerCharacter:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def run(self):
        print('run')

player1= PlayerCharacter('Cindy', 5)
player2= PlayerCharacter('Tom', 4)

people =[
    player1.name,
    player1.age,
    player2.name,
    player2.age
]

print(people)      