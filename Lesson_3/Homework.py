# while loop
# user input
# list of numbers
# list of num needs to be summed up
# calculate the average 
# x is a trigger
# and display it

numbers = []

while True: # while true, do smth
    user_input = input("Please enter a number: ")
    if user_input.lower() == 'x':
        print("Done")
        break
    numbers.append(int(user_input))
    print(numbers)
    
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"The sum is {total_sum}")
print(f"The average is {average}")
# ---------
# dictionary
# input from the user
# sque
user_input = int(input("Please enter a numberrr: "))
squares = {}

for counter in range(1, user_input +1):
    square = counter ** 2 # makeing a squere
    squares[counter] = square
    
print(f"squares are {squares}")
#-------------------
range()
