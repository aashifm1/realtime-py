
print("\nWelcome to College Hostel")
prog = input("What program are you in? (UG, PG): ").upper()

room_data = {
    'UG': {
        'AC': (UG_AC := [101, 102, 103, 104, 105], 150000),
        'NAC': (UG_NAC := [106, 107, 108, 109, 110], 125000),
    },
    'PG': {
        'AC': (PG_AC := [201, 202, 203, 204, 205], 100000),
        'NAC': (PG_NAC := [206, 207, 208, 209, 210], 75000),
    }
}

def hostel():
    year_limit = 5 if prog == 'UG' else 3
    year = int(input(f"What year are you in? (1-{year_limit}): "))
    
    if year < 1 or year > year_limit:
        print(f"Please enter a valid year (1 to {year_limit}).")
        return

    print(f"You are {prog} year {year} studying")
    room = input("\nDo you want an AC/Non-AC room? (AC/NAC): ").upper()
    
    if room in room_data[prog]:
        room_numbers, price = room_data[prog][room]
        room_no = int(input(f"\nEnter room n0 {room_numbers[0]} - {room_numbers[-1]}: "))
        
        if room_no in room_numbers:
            print(f"\nPayment of Rs.{price} for the room")
            print("Room booked\n")
        else:
            print(f"Enter a valid room no from {room_numbers[0]} - {room_numbers[-1]}\n")
    else:
        print("Room no is not available.\n")

hostel()
