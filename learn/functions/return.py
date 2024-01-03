def sum(num1,num2):
    print('hiii')
    return num1+num2

def sum1(num1,num2):
    def another_func(num1,num2):
        return num1+num2
    return another_func(num1,num2)

total=sum(10,20)
total1=sum1(40,10)

print(sum(330,20))
print(sum(40,total))
print(total)