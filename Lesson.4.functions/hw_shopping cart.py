"""# Shopping Cart Calculator
## Problem
You're building a shopping cart calculator for an online store. The program needs to:

1. Calculate the subtotal of items
2. Apply discounts based on different rules
3. Calculate tax
4. Add shipping costs
5. Display a formatted receipt

## Requirements
Without functions, this would involve repeating calculations and formatting code. Your task is to create functions that:

1. Eliminate repetitive calculations
2. Make the main program logic clear and easy to follow
3. Handle the price calculations step by step

## Expected Behavior
The program should allow users to add items to their cart, then display a detailed receipt with:
- Item list with prices
- Subtotal
- Discount applied (if any)
- Tax amount
- Shipping cost
- Final total

## Sample Run
```
Shopping Cart Calculator
========================

Enter item name (or 'checkout' to finish): Laptop
Enter price: 899.99

Enter item name (or 'checkout' to finish): Mouse
Enter price: 25.50

Enter item name (or 'checkout' to finish): Keyboard
Enter price: 75.00

Enter item name (or 'checkout' to finish): checkout

RECEIPT
=======
Laptop                           $899.99
Mouse                            $25.50
Keyboard                         $75.00
                               --------
Subtotal:                      $1000.49
Discount (10% for $1000+):      -$100.05
Tax (8.5%):                      $76.54
Shipping:                        $9.99
                               --------
TOTAL:                          $986.97
```

## Hints
Think about functions for:
- Calculating subtotals
- Determining and applying discounts
- Calculating tax
- Calculating shipping
- Formatting currency
- Printing receipt sections 
"""
def get_cart_items():
    cart = []
    while True:
        name = input("Enter item name (or 'checkout' to finish): ")
        if name.lower() == "checkout":
            break
        
        price = float(input("Enter price: "))
        cart.append((name, price))
    return cart

def calculate_subtotal(cart):
    return sum(price for name, price in cart)

def calculate_discount(subtotal):
    if subtotal >= 1000:
        return subtotal * 0.1
    else:
        return 0
    
def calculate_tax(discounted_total):
    return discounted_total * 0.085

def shipping():
    return 9.99

def print_receipt(cart, subtotal, discount, discounted_total, tax, shipping_cost, total):
    print("Shopping Cart Calculator")
    print("========================")
    for name, price in cart:
        print(name, " - ", price)
    print("Subtotal: ", subtotal)
    print ("Discount ", discount)
    print("Tax amount ", tax)
    print("Shipping ", shipping)
    print("Total ", total)
    

cart = get_cart_items()
subtotal = calculate_subtotal(cart)
discount = calculate_discount(subtotal)
discounted_total = subtotal - discount
tax = calculate_tax(discounted_total)
total = discounted_total - tax

