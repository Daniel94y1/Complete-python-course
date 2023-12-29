#pure functions

def multiply_by2(li):
    new_list=[]
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3,4,5]))

#function map()

my_list= [1,2,3,4,5]
def multiply_by2_map(item):
    return item*2

print(list(map(multiply_by2_map,my_list)))
print(my_list)

# function filter()

my_list1=[1,2,3,4,5,6,7,8,9,10]

def only_odd(item):
    return item % 2 !=0

print(list(filter(only_odd, my_list1)))
print(my_list1)

#function zip()

name= ['daniel', 'nil','yasir','sonia','lidia','lala']
email=['daniel@gmail.com', 'nil@gmail.com','yasir@gmail.com','sonia@gmail.com','lidia@gmail.com','lala@gmail.com']
phone=[888888888,111111111,222222222,333333333,444444444,555555555,777777777]
print(list(zip(name,email,phone)))

#function reduce()

from functools import reduce
my_list2=[1,2,3,4,5]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list2, 10))
print(my_list2)
