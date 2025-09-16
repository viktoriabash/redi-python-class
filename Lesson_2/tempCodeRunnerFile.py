while True:
    user_input = input ("Enter a string: ")
    
    if user_input == "":
        print ("Thanks for playing!")
        break
    
    print("First letter is capilized: ", user_input.capitalize())
    print(" All lowercase: ", user_input.lower())
    print("Title case: ", user_input.title())
    print("All uppercase: ", user_input.upper())