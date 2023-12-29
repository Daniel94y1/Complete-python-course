#list, set, dictionary

#list and set

my_list= []
my_list1= [char for char in 'pokemon']
my_list2= [num for num in range (0,200)]
my_list3=[num*2 for num in range (0,200)]
my_list4=[num**2 for num in range (0,200)]
my_list5=[num**2 for num in range (0,200) if num%2 ==0]

for char in 'hello':
    my_list.append(char)

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)

#dictionary

simple_dict ={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6
    }
my_dict={key:value**2 for key, value in simple_dict.items()}
my_dict1={k:v**2 for k,v in simple_dict.items() if v%2==0}
my_dict2={num:num*2 for num in [1,2,3,4,5]}

print(my_dict)
print(my_dict1)
print(my_dict2)

