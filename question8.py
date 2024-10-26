#input should only be a dictionary and an integer "n"
#returns a list of keys with values greater than
def greater_value(input_dict,n):
#for the value in a key that is greater than our n input should be returned in form of alist
    result = [key for key, value in input_dict.items() if value > n]
    return result
#promptr the user to enter the dictionary
input_str = input("Enter a dictionary in the format key1:value1, key2:value2, ... :")
#promptr the user to enter the value of n
n = int(input("Enter the value of n :"))
#convertnig the input into a dictionary
dict_items = input_str.split(", ")
user_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in dict_items}
#calling the function
result = (greater_value(user_dict,n))
print("This is the result",result)
