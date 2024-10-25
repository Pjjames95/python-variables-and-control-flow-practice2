def reverse_list(list):
    #reverse is only for an element in a string and not a whole list
    reverse_list = [element[::-1] for element in list]
    return reverse_list

list = ["apple","banana","cherry"]
#call the function
reverse_list = reverse_list(list)
print(reverse_list)




