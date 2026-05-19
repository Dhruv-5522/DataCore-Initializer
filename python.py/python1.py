print("Welcome to the Interactive Personal Data Collector!")
print()

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = input("Please enter your height in meters: ")
favourite_number = input("Please enter your favourite number: ")

age_int = int(age)
height_float = float(height)
fav_num_int = int(favourite_number)

current_year = 2026
birth_year = current_year - age_int

print()
print("Thank you! Here is the information we collected:")
print()

print("Name:", name, "(Type:", str(type(name)) + ", Memory Address:", str(id(name)) + ")")
print("Age:", age_int, "(Type:", str(type(age_int)) + ", Memory Address:", str(id(age_int)) + ")")
print("Height:", height_float, "(Type:", str(type(height_float)) + ", Memory Address:", str(id(height_float)) + ")")
print("Favourite Number:", fav_num_int, "(Type:", str(type(fav_num_int)) + ", Memory Address:", str(id(fav_num_int)) + ")")

print()
print("Your birth year is approximately:", birth_year, "(based on your age of", str(age_int) + ")")

print()
print("Thank you for using the Personal Data Collector. Goodbye!")
