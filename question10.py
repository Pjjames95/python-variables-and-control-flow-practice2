def tuple_to_dict(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        result_dict[key] = value
    return result_dict
#demonstration
demo_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
result = tuple_to_dict(demo_list)
print("Resulting dictionary:", result)