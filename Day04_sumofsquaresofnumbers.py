try:
    number = int(input("Enter a number to calculate sum of square upto: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        number = range(number + 1)
        squares = map(lambda x: x**2, number)
        print(f"Sum of squares from 0 to {number} is {sum(squares)}")
except ValueError:
    print("Error: nvalid input. enter please non-negative integer.")
