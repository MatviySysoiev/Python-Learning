def increate_person_age(person):
    print(id(person))  # e.g. 12345... (the same as person_one)
    # IT'S NOT RECOMMENDED TO EDIT OUTER VARIABLES IN THE FUNCTION
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21,
}

print(id(person_one))  # e.g. 12345... (the same as person)

increate_person_age(person_one)
print(person_one['age'])  # Was edited


# BETTER

def increate_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21,
}

new_person = increate_person_age(person_one)
print(new_person['age'])
print(person_one['age'])
