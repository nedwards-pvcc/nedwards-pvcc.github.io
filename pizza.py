
import datetime

######## define Global Variables #########

# define tax rate
SALES_TAX_RATE = 0.055

##### define program functions ########

def main():
    while True:
        num_pizzas, size = get_user_data()
        subtotal, sales_tax, total = perform_calculation(num_pizzas, size)
        display_results(num_pizzas, size, total)
        if not ask_user_for_another_order():
            break

def get_user_data():
    num_pizzas = int(input("Number of pizzas: "))
    size = input("Please enter size of pizza (S,M,L,X): ").lower() 
    return num_pizzas, size

def calculate_pizza_cost(size):
    cost = None
    if size == "s":
        cost = 9.99
    elif size == "S":
        cost = 9.99
    elif size == "m":
        cost = 12.99
    elif size == "M":
        cost = 12.99
    elif size == "l":
        cost = 14.99
    elif size == "L":
        cost = 14.99
    elif size == "x":
        cost = 17.99
    elif size == "X":
        cost = 17.99
    else:
        print("Invalid size entered. Please choose small (s), medium (m), large (l), or extra-large (x).")
    return cost

def perform_calculation(num_pizzas, size):
    pizza_cost = calculate_pizza_cost(size)  
    if pizza_cost is None:  
        return 0, 0, 0
    subtotal = num_pizzas * pizza_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    return subtotal, sales_tax, total

def display_results(num_pizzas, size, total):
    print('Number of Pizzas:  ' + str(num_pizzas))
    print('Size of Pizzas:    ' + size.upper()) 
    print('Total:            $' + format(total, ',.2f'))  
    print(str(datetime.datetime.now()))
def ask_user_for_another_order():
    user_input = input('Would you like to input data for another pizza order? (Y/N) ')
    return user_input.lower() == 'y'

######### call on main program to execute #########

main()
