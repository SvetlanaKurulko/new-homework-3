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



# v2 Створіть клас "Місто". Необхідно зберігати в полях класу:
# #    назву міста, назву регіону, назву країни, кількість жителів міста,
# #    поштовий індекс міста, телефонний код міста.
# #    Реалізуйте доступ до окремих полів (Інкапсуляція).


# class City:
#     def __init__(self, name, region, country, population, postal_code, phone_code):
#         self._name = name
#         self._region = region
#         self._country = country
#         self._population = population
#         self._postal_code = postal_code
#         self._phone_code = phone_code
#
#     def get_name(self):
#         return self._name
#
#     def get_region(self):
#         return self._region
#
#     def get_country(self):
#         return self._country
#
#     def get_population(self):
#         return self._population
#
#     def get_postal_code(self):
#         return self._postal_code
#
#     def get_phone_code(self):
#         return self._phone_code
#
#     def set_name(self, name):
#         if isinstance(name, str) and len(name) > 0:
#             self._name = name
#         else:
#             print("Invalid name.")
#
#     def set_region(self, region):
#         if isinstance(region, str) and len(region) > 0:
#             self._region = region
#         else:
#             print("Invalid region.")
#
#     def set_country(self, country):
#         if isinstance(country, str) and len(country) > 0:
#             self._country = country
#         else:
#             print("Invalid country.")
#
#     def set_population(self, population):
#         if isinstance(population, int) and population >= 0:
#             self._population = population
#         else:
#             print("Invalid population.")
#
#     def set_postal_code(self, postal_code):
#         if isinstance(postal_code, str) and len(postal_code) > 0:
#             self._postal_code = postal_code
#         else:
#             print("Invalid postal code.")
#
#     def set_phone_code(self, phone_code):
#         if isinstance(phone_code, str) and len(phone_code) > 0:
#             self._phone_code = phone_code
#         else:
#             print("Invalid phone code.")
#
#     def display_info(self):
#         print(f"City: {self._name}, Region: {self._region}, Country: {self._country}")
#         print(f"Population: {self._population}, Postal Code: {self._postal_code}, Phone Code: {self._phone_code}")
#
#
# city1 = City("Kyiv", "Kyiv Oblast", "Ukraine", 2800000, "02000", "+380")
# city1.display_info()
#
# print("City Name:", city1.get_name())
#
# city1.set_name("New Kyiv")
# city1.display_info()
#
# city1.set_population(-100)




# v2 2.Створіть клас "Країна". Необхідно зберігати в полях класу:
# #   назву країни, назву континенту, кількість жителів країни,
# #   телефонний код країни, назву столиці, назву міст країни.
# #   Реалізуйте доступ до окремих полів (Інкапсуляція).

# class Country:
#     def __init__(self, name, continent, population, phone_code, capital, cities):
#         self._name = name
#         self._continent = continent
#         self._population = population
#         self._phone_code = phone_code
#         self._capital = capital
#         self._cities = cities
#
#     def get_name(self):
#         return self._name
#
#     def get_continent(self):
#         return self._continent
#
#     def get_population(self):
#         return self._population
#
#     def get_phone_code(self):
#         return self._phone_code
#
#     def get_capital(self):
#         return self._capital
#
#     def get_cities(self):
#         return self._cities
#
#     def set_name(self, name):
#         if isinstance(name, str) and len(name) > 0:
#             self._name = name
#         else:
#             print("Invalid name.")
#
#     def set_continent(self, continent):
#         if isinstance(continent, str) and len(continent) > 0:
#             self._continent = continent
#         else:
#             print("Invalid continent.")
#
#     def set_population(self, population):
#         if isinstance(population, int) and population >= 0:
#             self._population = population
#         else:
#             print("Invalid population.")
#
#     def set_phone_code(self, phone_code):
#         if isinstance(phone_code, str) and len(phone_code) > 0:
#             self._phone_code = phone_code
#         else:
#             print("Invalid phone code.")
#
#     def set_capital(self, capital):
#         if isinstance(capital, str) and len(capital) > 0:
#             self._capital = capital
#         else:
#             print("Invalid capital.")
#
#     def set_cities(self, cities):
#         if isinstance(cities, list):
#             self._cities = cities
#         else:
#             print("Invalid cities list.")
#
#     def display_info(self):
#         print(f"Country: {self._name}, Continent: {self._continent}")
#         print(f"Population: {self._population}, Phone Code: {self._phone_code}")
#         print(f"Capital: {self._capital}")
#         print("Cities:")
#         for city in self._cities:
#             print(f"{city['name']}, Population: {city['population']}")
#
#
# cities_in_country = [
#     {"name": "Kyiv", "population": 2800000},
#     {"name": "Lviv", "population": 720000},
#     {"name": "Kharkiv", "population": 8398748}
# ]
#
# country = Country("Ukraine", "Europe", 41850000, "+380", "Kyiv", cities_in_country)
# country.display_info()
#
# print("Country Name:", country.get_name())
#
# country.set_name("Ukraine")
# country.display_info()
#
# country.set_population(-100)
