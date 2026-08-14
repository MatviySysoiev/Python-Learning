button = {
    'width': 200,
    'text': 'buy'
}

red_button = {
    **button,
    'color': 'red'
}

print(red_button)  # {'width': 200, 'text': 'buy', 'color': 'red'}

print(button)  # {'width': 200, 'text': 'buy'}

blue_button = {
    **red_button,
    'color': 'blue'
}

print(blue_button)  # {'width': 200, 'text': 'buy', 'color': 'blue'}


button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

button = button_info | button_style
# {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}
print(button)

button = {  # The same as |
    **button_info,
    **button_style
}

print(button)
# {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}
