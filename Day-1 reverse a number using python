number = int(input("Enter a number: "))  
  
# Step 1: Convert number to list of digits  
digit_list = [int(digit) for digit in str(number)]  
print("Original digits:", digit_list)  

# Step 2: Reverse the digits  
reversed_list = []  
for i in range(len(digit_list) - 1, -1, -1):  
    reversed_list.append(digit_list[i])  
print("Reversed digits:", reversed_list)  

# Step 3: Convert back to number  
reversed_number = 0  
for digit in reversed_list:  
    reversed_number = reversed_number * 10 + digit  

print("Reversed number:", reversed_number)
