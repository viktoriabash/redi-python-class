movies = {
        "Terminator 2": ["M", "E"],
        "Interstellar" : ["M", "A"],
        "Blacklist": ["M", "A", "E"],
        "Home Alone": ["E"],
        "The Pursuit of Happiness": ["M", "A"]
    }

seats_and_prices = {
    "regular" : 10,
    "vip" : 15,
    "dbpx" : 20
}

def movie_program():      # Function to display available movies and their showtimes to the user
    print("This is today's movie program:")
    for movie in movies:
        print(f"{movie} at show slot {movies[movie]}");

movie_program()

def choose_movie():      # Function to ask user for chosen movie and showtime, and validate the input
    title = input("Please choose the moovie: ")
    if title in movies:
        print("The moovie has been selected")
        show_time = input("Choose the show time: ")
        if show_time in movies[title]:
            print("The time is valid")
        else: 
            print("Time is not valid")          
    else:
        print("Moovie is not valid")



def seats():
    seat = input("Choose the type of the seat or skip")
    if seat == "":
        print("Regular seat is selected")
        seat = "regular"
    elif seat == "regular":
        print("Regular seat is selected")
    elif seat == "vip":
        print("VIP seat is selected")
    else:
        print("dbox seat is selected")
    return seat
        
        
def tickets_n():
    tickets = int(input("How many tickets do you want to buy? "))
    print(f"You chose ", tickets, " ticket/s!")
    return tickets

# def total_price():
#     if seats in seats_and_prices[]:
#         total = tickets_n * ticket_price
#         print(f"The price for the ", tickets, "is---", )
        
        
def total_price2(amount, seat_type):
    return amount * seats_and_prices[seat_type]

choose_movie()
seat_type = seats()
num_tickets = tickets_n()
total_price = total_price2(num_tickets, seat_type)
print(total_price)