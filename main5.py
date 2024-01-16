# 1. Даний текстовий файл. Необхідно створити новий файл,
#    який потрібно переписати з першого файлу всі слова,
#    що складаються не менше ніж з семи літер.


# with open('input.txt', 'w') as input_file:
#     input_file.write("To be, or not to be, that is the question, "
#                      "Whether 'tis nobler in the mind to suffer "
#                      "The slings and arrows of outrageous fortune, "
#                      "Or to take arms against a sea of troubles, "
#                      "And by opposing end them? To die: to sleep; "
#                      "No more; and by a sleep to say we end "
#                      "The heart-ache and the thousand natural shocks "
#                      "That flesh is heir to, 'tis a consummation "
#                      "Devoutly to be wish'd. To die, to sleep")
#
# with open('input.txt', 'r') as input_file:
#     text = input_file.read()
#
#     words = text.split()
#
#     filtered_words = [word for word in words if len(word) >= 7]
#
#     with open('output.txt', 'w') as output_file:
#         output_file.write(' '.join(filtered_words))
#
# print(" Результат знаходиться у файлі 'output.txt'.")

#
# #
# with open('input.txt', 'w') as input_file:
#     input_file.write("To be, or not to be, that is the question,\n"
#                      "Whether 'tis nobler in the mind to suffer\n"
#                      "The slings and arrows of outrageous fortune,\n"
#                      "Or to take arms against a sea of troubles,\n"
#                      "And by opposing end them? To die: to sleep;\n"
#                      "No more; and by a sleep to say we end\n"
#                      "The heart-ache and the thousand natural shocks\n"
#                      "That flesh is heir to, 'tis a consummation\n"
#                      "Devoutly to be wish'd. To die, to sleep")
# #
# with open('input.txt', 'r') as input_file:
#     text = input_file.read()
#
#     words = text.split()
#
#     filtered_words = [word for word in words if len(word) >= 7]
#
#     with open('output.txt', 'w') as output_file:
#         output_file.write('\n'.join(filtered_words))
#
# with open('output.txt', 'r') as output_file:
#     output_text = output_file.read()
#
#     print(output_text)

#
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

#
# with open('input.txt', 'r') as input_file:
#     text = input_file.read()
#
#     words = text.split()
#
#     word_count = len(words)
#
# print(f"Кількість слів у файлі 'output.txt': {word_count}")


# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
#
# def process_text_file(file_path, forbidden_word):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#
#             if forbidden_word.lower() in text.lower():
#                 processed_text = text.replace(forbidden_word, '*' * len(forbidden_word))
#                 print(f"Оброблений текст: {processed_text}")
#                 print(f"Кількість неприпустимих слів: {text.lower().count(forbidden_word.lower())}")
#             else:
#                 print("Неприпустимих слів не знайдено.")
#
#     except FileNotFoundError:
#         print(f"Файл '{file_path}' не знайдено.")
#
# file_path = 'input.txt'
#
# forbidden_word = 'die'
#
# process_text_file(file_path, forbidden_word)