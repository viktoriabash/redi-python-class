shopping_list = ["Cheese", "Tomatoes", "Bread", "Butter"]
student_names = ["Alice", "Bob","Charlie", "Alice", 45] #allowed: some items can be the same - we call it duplicates
student_grades = [1.0, 1.2, 1.3, "Passed"]

shopping_list.append("Cucumbers") #add item
shopping_list.insert(1, "Eggs") # specific place to add
shopping_list.remove("Bread") #remove item

# to find an element in the list
shopping_list.index("Butter")
print(shopping_list.index("Butter"))
student_names.index("Alice")
print(student_names.index("Alice"))

#to know how many elements are in the list - LEN
number_of_students = len(student_names) # 4
print(len(student_names))



# ti change the order of items in the list
student_names.reverse()
student_names.sort()


#to take a portion of the list
some_students.
some_students.

# alies goes to the store with a bag containing a pen
bag = ["Pen"]
#alies buys a notebook and puts in her bag
bag.append("Notebook")
# alice buys a laptop and puts it in her bag
bag.append("Laptop")
# alice buys a pencil and puts it in ther bag
bag.append("Pencil")
# on the way home, Alice  meets a friend and gives him a pen
bag.remove("Pen")
print(bag)
# but alice then hestistate if she has enough romm in her baf for anothe item. she checks
print(len(bag))
#OR
number_of_items = len(bag)
print(number_of_items)
# #ALice find the number of items in her bag and she want to remember if she ahs a laptop in ther bag
bag.index("Laptop") #1
print(bag.index("Laptop"), "Index of the laptop")

if "Laptop" in bag:
    print("Laptop found")
else:
    print("laptop not found")

#when alica gets home, she takes all the items out of her bag and shoes them to faily
print(bag)