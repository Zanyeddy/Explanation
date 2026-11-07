while True:
        try:
            user_input = input("Enter number greater than 1:")
            num = int(user_input)

            if user_input == e:
                break

            if num <= 1:
                print("number must e greater than 1.\n")
                continue
            for i in range(1, 13):
                print(f"{num}x{i}={num * i}")

        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
