# 1. Користувач вводить рядок з клавіатури.
# Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)


# user_input = input ("Enter a string:")
#
# letter_count = 0
# digit_count = 0
# for char in user_input:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count +=1
# print(f"letter_count: {letter_count}")
# print(f"digit_count: {digit_count}")

# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.

#
# user_input = input ("Enter a string:")
# search_char = input("Enter a token to search for:")
# char_count = 0
# for char in user_input:
#     if char == search_char:
#         char_count += 1
# print(f"token '{search_char}' meets {char_count} times in a string.")


# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

# user_input = input ("Enter a string:")
# search_word = input("Enter a word to search for:")
# replace_word = input("Enter a replacement word:")
# new_string = user_input.replace(search_word, replace_word)
# print("The resulting string:", new_string)


# Дано рядок. (зробити зрізи)
#
# input_string = input("Enter a string: ")
#
# # - Спершу виведіть третій символ цього рядка.
# print("Третій символ рядка:", input_string[2])
#
# # У другому рядку виведіть передостанній символ цього рядка.
# print("Передостанній символ цього рядка:", input_string[-2])
#
# # У третьому рядку виведіть перші п'ять символів цього рядка.
# print("Перші п'ять символів рядка:", input_string[:5])
#
# # У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# print("Весь рядок, крім двох останніх символів:", input_string[:-2])
#
# # У п'ятому рядку виведіть усі символи з парними індексами.
# print("Символи з парними індексами:", input_string[::2])
#
# # У шостому рядку виведіть усі символи з непарними індексами.
# print("Символи з непарними індексами:", input_string[1::2])
#
# # У сьомому рядку виведіть усі символи у зворотному порядку.
# print("Символи у зворотному порядку:", input_string[::-1])
#
# # У восьмому рядку виведіть усі символи рядка через один у зворотному порядку.
# print("Символи через один у зворотному порядку:", input_string[::-2])
#
# # У дев'ятому рядку виведіть довжину цього рядка.
# print("Довжина рядка:", len(input_string))


#Додатково:
#
# def modify_sentences(text):
#     sentences = text.split(". ")
#     modified_sentences = [sentence[:1].upper() + sentence[1:].lower() for sentence in sentences]
#     modified_text = ". ".join(modified_sentences)
#     return modified_text
#
# def count_digits(text):
#     digit_count = sum(1 for char in text if char.isdigit())
#     return digit_count
#
# def count_punctuation(text):
#     punctuation_count = sum(1 for char in text if char in '.,;:!?')
#     return punctuation_count
#
# def count_exclamation_marks(text):
#     exclamation_count = text.count('!')
#     return exclamation_count
#
# given_text = input("Введіть текст: ")
#
# # кожне речення починається з великої літери
# modified_text = modify_sentences(given_text)
# print("\nкожне речення з великої літери:\n", modified_text)
#
# # Кількість цифр у тексті
# digits_count = count_digits(given_text)
# print("\nКількість цифр у тексті:", digits_count)
#
# # Кількість розділових знаків у тексті
# punctuation_count = count_punctuation(given_text)
# print("\nКількість розділових знаків у тексті:", punctuation_count)
#
# # Кількість знаків оклику у тексті
# exclamation_count = count_exclamation_marks(given_text)
# print("\nКількість знаків оклику у тексті:", exclamation_count)