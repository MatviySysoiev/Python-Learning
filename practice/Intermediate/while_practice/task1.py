while True:
    try:
        num_one = float(input("Please enter first number:\n"))
        num_two = float(input("Please enter second number:\n"))
        if num_two == 0:
            print("\nDevision by zero! Please try again.\n")
            continue
        print(f"Division: {round(num_one/num_two, 2)}")
        user_answer = input("Would you like to continue? (Yes/No):\n")
        if user_answer.lower() == 'yes':
            continue
        else:
            break
    except ValueError as e:
        print("\nPlease enter a valid number!\n")
