first_list = ["Hello", "Matvii", "21.08.2026", "How are you?", 'a', 'c']

new_list = [elem for elem in first_list if len(elem) > 3]

print(new_list)
