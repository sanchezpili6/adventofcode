lanternfish = [1, 1, 5, 2, 1, 1, 5, 5, 3, 1, 1, 1, 1, 1, 1, 3, 4, 5, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 5, 4, 5,
               1, 5, 3, 1, 3, 2, 1, 1, 1, 1, 2, 4, 1, 5, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 3, 4, 5, 1, 1, 2, 1, 1, 5, 1,
               1, 4, 1, 4, 4, 2, 4, 4, 2, 2, 1, 2, 3, 1, 1, 2, 5, 3, 1, 1, 1, 4, 1, 2, 2, 1, 4, 1, 1, 2, 5, 1, 3, 2, 5,
               2, 5, 1, 1, 1, 5, 3, 1, 3, 1, 5, 3, 3, 4, 1, 1, 4, 4, 1, 3, 3, 2, 5, 5, 1, 1, 1, 1, 3, 1, 5, 2, 1, 3, 5,
               1, 4, 3, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 5, 2, 1, 5, 1, 4, 1, 1, 5, 1, 1, 1, 5, 5, 5, 1, 4,
               5, 1, 3, 1, 2, 5, 1, 1, 1, 5, 1, 1, 4, 1, 1, 2, 3, 1, 3, 4, 1, 2, 1, 4, 3, 1, 2, 4, 1, 5, 1, 1, 1, 1, 1,
               3, 4, 1, 1, 5, 1, 1, 3, 1, 1, 2, 1, 3, 1, 2, 1, 1, 3, 3, 4, 5, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 4, 1,
               5, 1, 3, 1, 1, 2, 5, 1, 1, 4, 1, 1, 4, 4, 3, 1, 2, 1, 2, 4, 4, 4, 1, 2, 1, 3, 2, 4, 4, 1, 1, 1, 1, 4, 1,
               1, 1, 1, 1, 4, 1, 5, 4, 1, 5, 4, 1, 1, 2, 5, 5, 1, 1, 1, 5]

lanternfish_example = [3,4,3,1,2]


def get_lanternfish_after_n_days(fish_arr, days):
    if days == 0:
        return len(fish_arr)
    else:
        for f, fish in enumerate(fish_arr):
            if fish >= 1:
                fish_arr[f] -= 1
            if fish == 0:
                fish_arr[f] = 6
                fish_arr.append(9)
        days -= 1
        return get_lanternfish_after_n_days(fish_arr, days)


def iterative_lanternfish_after_n_days(fish_arr, days):
    while days > 0:
        for f, fish in enumerate(fish_arr):
            if fish >= 1:
                fish_arr[f] -= 1
            if fish == 0:
                fish_arr[f] = 6
                fish_arr.append(9)
        days -= 1
    return len(fish_arr)


def quick_way(fish_arr, days):
    for day in range(days):



print(get_lanternfish_after_n_days(lanternfish_example, 80))
print(iterative_lanternfish_after_n_days(lanternfish, 256))
