 # 1. Напишіть функцію, яка обчислює добуток елементів списку цілих.
 # Список передається як параметр.
 # Отриманий результат повертається із функції.

# def calculate_product(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product
#
# my_list = [2, 3, 5, 7, 11]
#
# result = calculate_product(my_list)
# print("Добуток елементів списку:", result)


# 2. Напишіть функцію для знаходження мінімуму у списку цілих.
 # Список передається як параметр. Отриманий результат повертається із функції.

# def find_minimum(numbers):
#     if not numbers:
#         return None
#
#     minimum = numbers[0]
#
#     for num in numbers[1:]:
#         if num < minimum:
#             minimum = num
#
#     return minimum
#
#
# my_list = [5, 3, 8, 2, 7]
#
# result = find_minimum(my_list)
# print("Мінімальний елемент у списку:", result)

#
# 3.Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
 # Список передається як параметр. Отриманий результат повертається із функції.

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def count_primes(numbers):
#     count = 0
#     for num in numbers:
#         if is_prime(num):
#             count += 1
#     return count
#
# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# result = count_primes(my_list)
# print("Кількість простих чисел у списку:", result)


# 4. Напишіть функцію, яка видаляє зі списку ціле задане число.
 # З функції потрібно повернути кількість видаленних елементів.

# def remove_element(nums, target):
#     count_deleted = nums.count(target)
#     nums[:] = [num for num in nums if num != target]
#     return count_deleted
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 4, 8, 9, 4, 10]
# to_remove = 4
#
# deleted_count = remove_element(my_list, to_remove)
# print(f"Кількість видалених елементів: {deleted_count}")
# print(f"Список після видалення: {my_list}")


# 5.Напишіть функцію, яка отримує два списки як параметр і повертає список,
 # що містить елементи обох списків.

# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list
#
# first_list = [1, 2, 3]
# second_list = [4, 5, 6]
#
# result = merge_lists(first_list, second_list)
# print("Об'єднаний список:", result)

# 6.Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
 # Значення для ступеня передається як параметр, список також передається як параметр.
 # Функція повертає новий список, який містить отримані результати.

#
# def calculate_power(nums, power):
#     powered_list = [num ** power for num in nums]
#     return powered_list
#
# my_list = [1, 2, 3, 4, 5]
# exponent = 3
#
# result = calculate_power(my_list, exponent)
# print("Список чисел піднесених до степеня:", result)