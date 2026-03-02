def find_minimum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    min_of_rest = find_minimum_recursive(lst[1:])
    if lst[0] < min_of_rest:
        return lst[0]
    else:
        return min_of_rest
print(find_minimum_recursive([20,10,2132,31231,2312321,3213123,3123]))