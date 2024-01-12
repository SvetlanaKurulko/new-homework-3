# 1. домашній номер телефону (тільки цифри та довжина номера)


# import re
#
# def validate_home_phone(phone_number):
#
#     pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{2}-\d{2}$')
#
#     if pattern.match(phone_number):
#         return True
#     else:
#         return False
#
# home_phone = "(044) 528-36-59"
# result = validate_home_phone(home_phone)
#
# if result:
#     print(f"{home_phone} є валідним домашнім номером телефону.")
# else:
#     print(f"{home_phone} не є валідним домашнім номером телефону.")



# 2. - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)


# import re
#
# def validate_mobile_phone(phone_number):
#     pattern = re.compile(r'^\+?\d{12}$')
#
#     if pattern.match(phone_number):
#         return True
#     else:
#         return False
#
# mobile_phone = "+380636268470"
# result = validate_mobile_phone(mobile_phone)
#
# if result:
#     print(f"{mobile_phone} є валідним мобільним номером телефону.")
# else:
#     print(f"{mobile_phone} не є валідним мобільним номером телефону.")

#
# 3. - email (наявність @, домену: gmail.com наприклад,
#      мінімальна довжина та максимальна на ваш вибір)
#
# import re
#
# def validate_email(email):
#     pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
#
#     if pattern.match(email):
#         return True
#     else:
#         return False
#
# email_address = "shepit.ukraine@gmail.com"
# result = validate_email(email_address)
#
# if result:
#     print(f"{email_address} є валідним email.")
# else:
#     print(f"{email_address} не є валідним email.")


# 4.- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

# import re
#
# def validate_full_name(full_name):
#     pattern = re.compile(r'^[а-яА-ЯёЁa-zA-Z]{2,20}\s[а-яА-ЯёЁa-zA-Z]{2,20}\s[а-яА-ЯёЁa-zA-Z]{2,20}$')
#
#     if pattern.match(full_name):
#         return True
#     else:
#         return False
#
# client_name = "Kurulko Svitlana Volodymyrivna"
# result = validate_full_name(client_name)
#
# if result:
#     print(f"{client_name} є валідним ПІБ.")
# else:
#     print(f"{client_name} не є валідним ПІБ.")

# 5. Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра,
#    один символ, довжина пароля – від 8 до 16 символів)

# import re
#
# def validate_password(password):
#
#     pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=])[a-zA-Z\d!@#$%^&*()-_+=]{8,16}$')
#
#     if pattern.match(password):
#         return True
#     else:
#         return False
#
# user_password = "Shepit2#!"
# result = validate_password(user_password)
#
# if result:
#     print(f"{user_password} є валідним паролем.")
# else:
#     print(f"{user_password} не є валідним паролем.")