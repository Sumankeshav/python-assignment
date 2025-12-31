num1=float(input("enter first number"))
num2=float(input("enter second number"))
add=num1+num2
sub=num1-num2
mul=num1*num2

if num2 !=0:
    div=num1/num2
else:
    div="Cannot divide by zero"

print("The sum is",add)
print("The difference is",sub)
print("The multiplication is",mul)
print("The division is",div)