def greeting(greet):
    return lambda name: f"{greet}, {name}"


morning_greeting = greeting("Good morning")  # new function
print(morning_greeting('Matvii'))

evening_greeting = greeting("Good evening")  # new function
print(evening_greeting('Matvii'))
