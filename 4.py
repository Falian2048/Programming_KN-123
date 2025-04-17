numbers = list(map(int, input().split()))

unique_numbers = []

for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)


print(*unique_numbers)
