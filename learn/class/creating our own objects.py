#00P
class PlayerCharacter:
    # Class Object Attribute
    membership=True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name=name
            self.age=age
        
    
    def shout(self):
        print(f'my name is {self.name}')

player1= PlayerCharacter('Cindy', 5)
player2= PlayerCharacter('Tom', 4)

print(player1.shout())
print(player2.shout())



  