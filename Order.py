from App import Customer , Pizza

customers = [ ]
pizza_price_List = [ 10 , 12 , 15 , 18 ]

def customer_Info():

    name = input("Enter your name: ")
    
    Email = input("Enter your email: ")
    
    Address = input("Enter your address: ")
    
    size = input("Enter pizza size (Small, Medium, Large, X-Large): ")

    for i in pizza_price_List :
        if size ==  "Small":
            cost = pizza_price_List[0]
            break
        elif size == "Medium":
            cost = pizza_price_List[1]   
            break
        elif size == "Large":
            cost = pizza_price_List[2]
            break
        elif size == "X-Large":
            cost = pizza_price_List[3] 
            break

    price = cost        

    number_of_pizza = int(input("Enter the quantity: "))

    cu = Customer(name , Email , Address)
    customers.append(cu)
    
    pI = Pizza(size , price , number_of_pizza)
    customers.append(pI)
    
def display_order_details():

    print("\nOrder Details:\n")

    for cu in customers:
        print(cu)
    print("\n")
    for order_details in customers: 
        print(order_details)
        
while True : 

    print("\nSelect an option\n")
    print ("1 to Enter Customer Details\n")
    print ("2 to Display order details and Total Price\n")
    print ("3 to Exit\n")
    
    x = input("==>")

    if x == "1":
        customer_Info()

    elif x == "2":
        display_order_details()

    elif x == "3":
        print("Thanks For Ordering")
        break    
    
    else:
        print("You Made a Mistake , Try Again")
