class PlayerCharacter:
    def __init__(self, name, age):
        self._name=name # private variable
        self._age=age
    
    def run(self):
        print('run')
    def speak(self):
        print(f'my name is {self.name} and i am {self.age} years old')

player1=PlayerCharacter('andrei', 100)    
player1.name='!!!'
player1.speak='BOOOOO'
print(player1.name)



