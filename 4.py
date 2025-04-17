# Given a list of numbers, all on one line
numbers = input().split()

# Create a list to store numbers that are unique
unique_numbers = []

for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

# Print the unique numbers in the order they appear
print(*unique_numbers)
