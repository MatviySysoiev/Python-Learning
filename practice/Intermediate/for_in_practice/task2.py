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
