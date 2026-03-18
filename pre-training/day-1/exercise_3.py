# Multiplication table generator

while True:
    choice = input("Enter a number (1-12) or 'all' for all tables: ").lower()
    
    if choice == 'all':
        # Print all tables
        for num in range(1, 13):
            print(f"\nTable of {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
        break
    try:
        num = int(choice)
        if num >= 1 and num <= 12:
            # Print the table for this number
            print(f"\nTable of {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
            break
        else:
            print("Please enter a number between 1 and 12")
    except ValueError:
        print("That's not a valid number, try again")
