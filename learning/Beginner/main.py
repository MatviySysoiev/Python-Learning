name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(name)
print(age)
print(city)

print(name.capitalize()) # capitalize делает первую букву заглавной, также переменная name не изменилась
print(name.upper()) # upper делает все буквы заглавными
print(dir(name))