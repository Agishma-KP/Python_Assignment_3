#Excercise 2
age = int(input("Enter your age: "))

if age < 16:
    price = 6 / 2
elif age >= 60:
    price = 6 / 3
else:
    price = 6

print(f"Your ticket costs £{price:.2f}")

#Excercise 4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The greatest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The greatest number is {num2}")
else:
    print(f"The greatest number is {num3}")
