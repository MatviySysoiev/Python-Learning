def filter_list(new_list, spec_type):
    result = []
    for i in new_list:
        if type(i) == int:
            result.append(i)
        # Not recommended, because bool is subclass of int
        # if isinstance(i, spec_type):
        #     result.append(i)
    return result


new_list = [True, 1, 5, '3', False, 51]

print(filter_list(new_list, int))


def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


res = filter_list(new_list, int)
print(res)
