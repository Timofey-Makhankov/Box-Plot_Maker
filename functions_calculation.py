def median_even(items: list, length: int):
    index_1: int = length // 2 - 1
    index_2: int = length // 2
    return (items[index_1] + items[index_2]) / 2


def median_odd(items: list, length: int):
    index_1: int = length // 2
    return (items[index_1])


def item_max(items: list):
    return max(items)


def item_min(items: list):
    return min(items)


def upper_quartile_even(items: list):
    half_list = []
    half_list.extend(items[len(items)//2:])
    length_of_half = len(half_list)
    index_1 = length_of_half // 2 - 1
    index_2 = length_of_half // 2
    return float((half_list[index_1] + half_list[index_2]) / 2)


def upper_quartile_odd(items: list):
    half_list = []
    half_list.extend(items[len(items)//2+1:])
    length_of_half = len(half_list)
    index_1 = length_of_half // 2 - 1
    index_2 = length_of_half // 2
    return float((half_list[index_1] + half_list[index_2]) / 2)


def lower_quartile_even(items: list):
    half_list = []
    half_list.extend(items[:len(items)//2])
    length_of_half = len(half_list)
    index_1 = length_of_half // 2 - 1
    index_2 = length_of_half // 2
    return float((half_list[index_1] + half_list[index_2]) / 2)


def lower_quartile_odd(items: list):
    half_list = []
    half_list.extend(items[:len(items)//2+1])
    length_of_list = len(half_list)
    index_1 = length_of_list // 2 - 1
    index_2 = length_of_list // 2
    return float((half_list[index_1] + half_list[index_2]) / 2)