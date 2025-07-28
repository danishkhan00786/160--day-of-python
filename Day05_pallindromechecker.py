expression = input("enter a expression").replace("","").lower()
print(f"your given expression ({expression}) now checking for pallindrome")

if expression == expression[::-1]:
  print("✅ Yes, given expression is pallindrome")
else :
  print("❌not pallindrome")
