month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

month = int(input("Enter the month (1-12): "))
if 1 <= month <= 12:
    print(f"Month {month} is {month_names[month - 1]}")
else:
    print("Invalid input! Please enter a number between 1 and 12.")
