numbers_list = input("Введіть цілі числа через пропуск: ").split()

product = "*".join(numbers_list)

print("Добуток чисел:", eval(product))