# 1. Створіть клас "Місто". Необхідно зберігати в полях класу:
#    назву міста, назву регіону, назву країни, кількість жителів міста,
#    поштовий індекс міста, телефонний код міста.
#    Реалізуйте доступ до окремих полів (Інкапсуляція).


# class City:
#     def __init__(self, name, region, country, population, postal_code, phone_code):
#         self._name = name
#         self._region = region
#         self._country = country
#         self._population = population
#         self._postal_code = postal_code
#         self._phone_code = phone_code
#
#     def display_info(self):
#         print(f"City: {self._name}, Region: {self._region}, Country: {self._country}")
#         print(f"Population: {self._population}, Postal Code: {self._postal_code}, Phone Code: {self._phone_code}")
#
#
# city1 = City("Kyiv", "Kyiv Oblast", "Ukraine", 2800000, "02000", "+380")
# city2 = City("Lviv", "Lviv Oblast", "Ukraine", 720000, "79000", "+380")
# city3 = City("New York", "New York State", "USA", 8398748, "10001", "+1")
#
# city1.display_info()
# print("\n")
# city2.display_info()
# print("\n")
# city3.display_info()



#   2.Створіть клас "Країна". Необхідно зберігати в полях класу:
#   назву країни, назву континенту, кількість жителів країни,
#   телефонний код країни, назву столиці, назву міст країни.
#   Реалізуйте доступ до окремих полів (Інкапсуляція).


# class Country:
#     def __init__(self, name, continent, population, phone_code, capital, cities):
#         self._name = name
#         self._continent = continent
#         self._population = population
#         self._phone_code = phone_code
#         self._capital = capital
#         self._cities = cities
#
#     def display_info(self):
#         print(f"Country: {self._name}, Continent: {self._continent}")
#         print(f"Population: {self._population}, Phone Code: {self._phone_code}")
#         print(f"Capital: {self._capital}")
#         print("Cities:")
#         for city in self._cities:
#             print(f"{city['name']}, Population: {city['population']}")
#
# cities_in_country = [
#     {"name": "Kyiv", "population": 2800000},
#     {"name": "Lviv", "population": 720000},
#     {"name": "Kharkiv", "population": 8398748}
# ]
#
# country = Country("Ukraine", "Europe", 41850000, "+380", "Kyiv", cities_in_country)
#
# country.display_info()