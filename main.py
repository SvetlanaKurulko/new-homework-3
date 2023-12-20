# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.


# while True:
#     try:
#         print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday"
#           "\n7. Sunday")
#         user_select = int(input("Enter menu number: "))
#
#         match user_select:
#             case 1:
#                  print ("Monday")
#             case 2:
#                  print("Tuesday")
#             case 3:
#                 print("Wednesday")
#             case 4:
#                 print("Thursday")
#             case 5:
#                 print("Friday")
#             case 6:
#                 print("Saturday")
#             case 7:
#                 print("Sunday")
#             case _:
#                 raise ValueError("Invalid value. Enter a number from 1 to 7.")
#
#     except Exception as e:
#                 print(f"Error: {e}")




# Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні,
# вивести їх на екран у порядку зростання


# while True:
#     try:
#         num1 = float(input("Введіть перше число: "))
#         num2 = float(input("Введіть друге число: "))
#
#         if num1 == num2:
#             print("Числа рівні.")
#         else:
#             sorted_numbers = sorted([num1, num2])
#             print("Числа у порядку зростання:", sorted_numbers)
#
#     except ValueError:
#         print("Невірне введення. Будь ласка, введіть числа.")



# 3. Користувач вводить два числа та матем дію: + - * або /
#
# Залежно від введеної матем дії вивести результат
# while True:
#     try:
#         num1 = float(input("Введіть перше число: "))
#         num2 = float(input("Введіть друге число: "))
#         operation = input("Введіть операцію (+, -, *, /): ")
#
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             if num2 == 0:
#                 result = "Помилка: ділення на нуль"
#             else:
#                 result = num1 / num2
#         else:
#             result = "Невірна операція"
#
#         print("Результат:", result)
#
#     except ValueError:
#         print("Невірне введення. Будь ласка, введіть числа.")
