def say_hello():
    print('helloooo')

say_hello()

# christmas tree
picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def show_tree():
    for row in picture:
        for pixel in row: 
            if(pixel==1):
                print('*', end='')           
            else:
                print(' ', end='') 
        print('')

show_tree()
show_tree()
show_tree()

#parameters
#default parameters
def say_hello(name='Darth Vader', emoji=':)'):
    print(f'hellooooo {name} {emoji}')

#positional arguments
say_hello('Andrei','·_·')
say_hello('Dan','·_·')
say_hello('Emily','·_·')

# keyword arguments
say_hello(emoji='·_·', name='Bibi')
say_hello()
   

