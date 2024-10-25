#numbers begins from 1 to 50 hence range reaches 51
for numbers in range(1,51):
    #divisibility for 3
    #if ......else applies
    if numbers % 3 == 0:
        print("fizz")
        # divisibility for 5
    elif numbers % 5 == 0:
        print("buzz")
    elif numbers % 3 == 0 and numbers % 5 == 0:
            print("fizzbuzz")
            #if a number does not satisfy both of them then it should be printed as it is.
    else:
        print(numbers)