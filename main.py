from itertools import count

sum_of_even_numbers = 0

for number in range(1, 101):
    if number %2 == 0:
        sum_of_even_numbers += number

print("Сумма всех четных чисел от 1 до 100:", sum_of_even_numbers)

squares_of_odd_numbers = [i**2 for i in range(1,11) if i % 2 !=0]
print("Квадраты всех нечетных чисел от 1 до 10:", squares_of_odd_numbers)

count = 0
while True:
    number = float(input("Введите число: "))
    if number < 0:
        break
    count +=1
print(f"Количество введеных чисел : {count}")