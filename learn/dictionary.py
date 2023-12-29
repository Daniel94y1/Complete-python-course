#dictionary

dictionary ={ #dictionary is a collection of key-value pairs
    "a":"apple",
    "b":"banana",
    "c":"carrot",
}
print(dictionary['a']) #prints apple

my_list = [{
        "a":"apple",
        "b":"banana",
        "c":"carrot"
    },{
        "a":[1,2,3],
        "b":"banana",
        "c":"carrot",
    }]
print(my_list[1]['a'][2]) #prints 3