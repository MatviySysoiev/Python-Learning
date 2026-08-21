def dict_to_list(dictionary):
    if not isinstance(dictionary, dict):
        return "Dictionary wasn't found!"

    result = []
    for k, v in dictionary.items():
        if type(v) == int:
            v = v * 2
        result.append((k, v))

    return result


new_dict = {
    'A': "Hello",
    'B': 54,
    5: 'gg'
}

res = dict_to_list(new_dict)
print(res)
