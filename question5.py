def even_value_keys(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:
            print(key)
#prompting the user to enter their dictionary.
input_str = input("Enter a dictionary in the format key1:value1, key2:value2, ... : ")

#convert the input into a dictionary
dict_items = input_str.split(", ")
user_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in dict_items}

#call the function
even_value_keys(user_dict)
