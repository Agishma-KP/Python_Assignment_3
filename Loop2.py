#Exercise 8
while True:
    value = input("Enter a value: ")
    if value.lower() == "done":
        print("Done")
        break
    print(value)

#Exercise 9
for num in range(1, 11):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Exercise 10
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()