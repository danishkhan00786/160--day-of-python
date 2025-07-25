number = int(input("Enter a number: "))

# Use absolute value for digit extraction
abs_number = abs(number)

# Extract digits
digits = [int(digit) for digit in str(abs_number)]

# Show each digit
print("Each digit of your number:", digits)

# Calculate sum of digits
digit_sum = sum(digits)

# Output result
print("Sum of digits of your given number =", digit_sum)
