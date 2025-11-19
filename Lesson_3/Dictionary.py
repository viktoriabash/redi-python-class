# Game

# We want to store the highests

best_player = ("Alice", 1500, "16.09.2025", "Munich", 5)


# Very soon, the data gets more complex, and it is hard to remember what each value means

# We can use a dictionary instead

best_player = {

"name": "Alice",

"score": 1500,

"date": "16.09.2025",

"city": "Munich",

"level": 5

}


# To access a value, we use its key

player_name = best_player["name"] # "Alice"

player_score = best_player["score"] # 1500


# To set an existing key to a new value

best_player["score"] = 1600 # Now the score is 1600


# To add a new key-value pair

best_player["lives"] = 3 # Now the dictionary has a new key "lives" with value 3
# To get all values:

player_scores = {

"Alice": 1600,

"Bob": 1200,

"Charlie": 800

}

player_score_values = player_scores.values() # dict_values([1600, 1200, 800])

# You can use it in a for loop. Otherwise, convert it to a list:

list_of_values = list(player_scores.values()) # [1600, 1200, 800]

# Please rather use values() as a list, only when they all have the same type (e.g. all numbers)


# To get all key-value pairs:

player_items = best_player.items() # dict_items([('name', 'Alice'), ('score', 1600), ('date', '16.09.2025'), ('city', 'Munich'), ('level', 5), ('lives', 3)])

# You can use it in a for loop.

for key, value in best_player.items():

print(f"{key}: {value}")


# To remove a key-value pair

removed_score = best_player.pop("score") # removed_score is 1600, and the "score" key is removed from the dictionary

# If the key does not exist, it throws a KeyError

removed_non_existing = best_player.pop("non_existing", None) # removed_non_existing is None, no error is thrown

# To update the dictionary with another dictionary

additional_info = {

"country": "Germany",

"age": 25

}

best_player.update(additional_info)

# Important: if a key already exists, its value is overwritten

more_info = {

"age": 26,

"lives": 4

}

best_player.update(more_info) # Now "age" is 26, and "lives" is 4


# We can have a dictionary of dictionaries. We call it a nested dictionary

players = {

"Alice": {"score": 1600, "level": 5},

"Bob": {"score": 1200, "level": 4},

"Charlie": {"score": 800, "level": 3},

}


bag_contents = {

"Alice": ("pen", "notebook", "laptop", "pencil"),

"Bob": ("book", "laptop"),

"Charlie": ("notebook", "pencil")

}
car_preferences = {
    "color": red,
    "num_of_doors": 4
    }
    
bob_preferences = {
    "brand": BMW,
   "sunroof": True
}
car_preferences.update(bob_preferences)
car_preferences["price"] = 200000 # add price
car_preferences.pop("brand")  #remive brand from dictionary
car_preferences["price"] = 180000 # set new value for price

for key, value in car_preferences.items():
print(f"{key}: {value}")
 #print out everything
#----------------------------
