# def keyword _ function name (function param)
# firt line function signiture
def greet(name): # greet is the name of function
    greeting = f"Helo {name.capitalize()}"
    print(greeting)
    return greeting


def I_Shall_not(times, text): # function, name, parametres
    for index in range(1, times + 1):
        print(f"{index} - {text}")
        
I_Shall_not(2, "I shall not break things")
