#У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;

# import random
#
# def sum_of_negatives(nums):
#     return sum(num for num in nums if num < 0)
#
# random_numbers = [random.randint(-10, 10) for _ in range(20)]
#
# print("Список випадкових чисел:", random_numbers)
# print("Сума негативних чисел:", sum_of_negatives(random_numbers))

# ■ Суму парних чисел;

# import random
#
# def sum_of_even_numbers(nums):
#     return sum(num for num in nums if num % 2 == 0)
#
# random_numbers = [random.randint(1, 100) for _ in range(20)]
#
# print("Список випадкових чисел:", random_numbers)
# print("Сума парних чисел:", sum_of_even_numbers(random_numbers))

# ■ Суму непарних чисел;

# import random
#
# def sum_of_odd_numbers(nums):
#     return sum(num for num in nums if num % 2 != 0)
#
# random_numbers = [random.randint(1, 100) for _ in range(20)]
#
# print("Список випадкових чисел:", random_numbers)
# print("Сума непарних чисел:", sum_of_odd_numbers(random_numbers))

#  Добуток елементів з кратними індексами 3;
# import random
#
# def product_of_indices_3(nums):
#     return nums[0] * nums[3] * nums[6]
#
#
# random_numbers = [random.randint(1, 10) for _ in range(10)]
#
# print("Список випадкових чисел:", random_numbers)
# print("Добуток елементів з кратними індексами 3:", product_of_indices_3(random_numbers))

# Добуток елементів між мінімальним та максимальним елементом;
# import random
#
# def product_between_min_max(nums):
#     min_num = min(nums)
#     max_num = max(nums)
#
#     min_index = nums.index(min_num)
#     max_index = nums.index(max_num)
#
#     start_index = min(min_index, max_index) + 1
#     end_index = max(min_index, max_index)
#
#     product = 1
#
#     for num in nums[start_index:end_index]:
#         product *= num
#
#     return product
#
# random_numbers = [random.randint(1, 100) for _ in
#                   range(10)]
#
# print("Список випадкових чисел:", random_numbers)
# print("Добуток елементів між мінімальним та максимальним елементом:",
#       product_between_min_max(random_numbers))

# Суму елементів, що знаходяться між першим та останнім позитивними елементами.
# import random
# def sum_between_first_last_positive(nums):
#     first_positive_index = -1
#     last_positive_index = -1
#
#     for i, num in enumerate(nums):
#         if num > 0:
#             if first_positive_index == -1:
#                 first_positive_index = i
#             else:
#                 last_positive_index = i
#
#     if first_positive_index != -1 and last_positive_index != -1:
#         return sum(nums[first_positive_index + 1:last_positive_index])
#     else:
#         return 0
#
# random_numbers = [random.randint(-10, 10) for _ in
#                   range(20)]
#
# print("Список випадкових чисел:", random_numbers)
# print("Сума елементів між першим та останнім позитивними елементами:",
#       sum_between_first_last_positive(random_numbers))

# Завдання 2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:


# import random
#
#
# # Генерація списку цілих чисел
# random_numbers = [random.randint(-10, 10) for _ in range(20)]  # Приклад: створення списку з 20 випадкових чисел від -10 до 10
#
# # Створення списку лише з парних чисел
# even_numbers = [num for num in random_numbers if num % 2 == 0]
#
# # Створення списку лише з непарних чисел
# odd_numbers = [num for num in random_numbers if num % 2 != 0]
#
# # Створення списку лише з негативних чисел
# negative_numbers = [num for num in random_numbers if num < 0]
#
# # Створення списку лише з позитивних чисел
# positive_numbers = [num for num in random_numbers if num > 0]
#
# print("Список випадкових чисел:", random_numbers)
# print("Список лише з парних чисел:", even_numbers)
# print("Список лише з непарних чисел:", odd_numbers)
# print("Список лише з негативних чисел:", negative_numbers)
# print("Список лише з позитивних чисел:", positive_numbers)