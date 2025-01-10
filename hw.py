def check_birth_day():
    try:
        user_input = input("Enter the day of your birth (1-31): ")
        birth_day = int(user_input)
        
        # Check if the day is within the valid range
        if 1 <= birth_day <= 31:
            if birth_day % 2 == 0:
                print(f"The day {birth_day} is even.")
            else:
                print(f"The day {birth_day} is odd.")
        else:
            print("The input is not a valid day of the month. Please enter a number between 1 and 31.")
    except ValueError:
        print("The input is not a valid number. Please enter a numeric value.")

check_birth_day()
