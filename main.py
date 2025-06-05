sum_of_even_numbers = sum([number for number in range(1, 101) if number % 2 == 0])

squares_of_odd_numbers = [i ** 2 for i in range(1, 11) if i % 2 != 0]

count = 0
while True:
    number = float(input("Введите число: "))
    if number < 0:
        break
    count += 1

print(f"Сумма всех четных чисел от 1 до 100: {sum_of_even_numbers},"
      f" Квадраты всех нечетных чисел от 1 до 10: {squares_of_odd_numbers} "
      f"Количество введеных чисел : {count}")
