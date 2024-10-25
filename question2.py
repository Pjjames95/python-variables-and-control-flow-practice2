#prompt for input from user
#process should repeat until the word exit is typed
while True:
    #user is prompted to enter a word
    word = input("Enter a word: ")
    if word == "exit":
        break
    print(word)
