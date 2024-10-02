
print("\nCarBuy 360")
n=input("Do you want to buy a car? (Yes/No): ").lower()

car={
    'BMW 5 Series':1340000,
    'Audi A4':17000000,
    'Volvo XC90':15200000,
    'Porsche 911':19900000
}

def carbuy():
    if n == 'yes':
        
        print("\nSure. Visit our showroom. We have 4 car model available.")
        pick=input("Pick one (BMW 5 Series, Audi A4, Volvo XC90, Porsche 911): ")
        
        if pick in car:
            price=car[pick]
            print("\nThe price of",pick,"is",price)
            conf=input("Do you sure of buying: ").lower()
            
            if conf == 'yes':
                print("Payment Process Started...\n")
                payment()
            else:
                print("Okay. Thanks for visiting. Have a nice day.\n")
        
        else:
            print("The car is not available here.\n")
    
    else:
        print("Okay. No problem.\n")

def payment():
    pay=input("Enter your debit card (12-Digits):")
    if len(pay) == 12 and pay.isdigit():
        print("Money paid. Car will be delivered to your address\n")
        return pay
    else:
        print("Invalid card detail. Try again later\n")


carbuy()