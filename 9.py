binary_numbers = input().split(',')


def binary_to_decimal(binary):
    return int(binary.strip(), 2)


divisible_by_5 = []
for binary in binary_numbers:
    decimal = binary_to_decimal(binary)
    if decimal % 5 == 0:
        divisible_by_5.append(binary.strip())

print(','.join(divisible_by_5))
