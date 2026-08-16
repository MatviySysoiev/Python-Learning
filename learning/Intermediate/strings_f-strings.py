my_name = 'Matvii'
my_hobby = 'swimming'
time = 8

info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + ' o\'clock'

new_info = f"{my_name} likes {my_hobby} at {time} o'clock"  # The same
# Also f-strings allows you to use different types without convertation

print(info)
print(new_info)

task_info = f"{my_name.capitalize()} Likes {my_hobby.capitalize()} At {str(time).capitalize()} O'clock"
print(task_info)
