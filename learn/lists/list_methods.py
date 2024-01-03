basket= [1,2,3,4,5]
print(len(basket)) #len returns the lenght of the list

#adding
basket.append(100) #append adds and object to the end of the list
basket.insert(2,300) #insert adds and object to the list at the specified index
basket.extend([400,401]) #extends adds a list to the end of the list


new_list= basket
print(basket)
print(new_list)

#removing
basket.pop() #pop removes the last object of the list
basket.pop(0) #or the object of the specified index
basket.remove(2) #remove removes the specified object

new_list1=basket
new_list1.clear() #clear removes all the objects of the list
print(basket)
print(new_list1)