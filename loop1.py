#Exercise 5
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

#Exercise 6
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    reversed_num = (reversed_num * 10) + (num % 10)
    num //= 10

print(f"The reversed number is {reversed_num}")

#Exercise 7
num = int(input("Enter a number: "))
count = int(input("Enter how many multiples you want: "))

print(f"The first {count} multiples of {num} are:")
for i in range(1, count + 1):
    print(num * i)


