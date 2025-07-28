expression = input("enter a expression").replace("","").lower()
print(f"your given expression ({expression}) now checking for pallindrome")
reverse_expression = []
for i in range(len(expression)-1,-1,-1):
 reverse_expression.append(expression[i])
i = 0
is_pallindrome = True
while i<len(reverse_expression):
 if reverse_expression[i] != expression[i] :
    is_pallindrome = False
break
i+=1
if is_pallindrome:
  print("✅given expression is pallindrome")
else :
  print("❌not pallindrome")
