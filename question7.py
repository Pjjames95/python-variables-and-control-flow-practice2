from enum import unique


def remove_duplicates(input_list):
    #a unique list must be associated with our output
    unique_lst = []
    for item in input_list:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
#prompting the user to enter their list
input_list = input("Enter a list in the format value1, value2, value3, ...:")
result = remove_duplicates(input_list)
print("This is the unique list", result)
