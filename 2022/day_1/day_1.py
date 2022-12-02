def open_input_file():
    f = open("input.txt", "r")
    return f.readlines()


def group_input(input):
    groups = []
    group = []
    for line in input:
        if line == "\n":
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
    groups.append(group)
    return groups


def sum_each_group(groups):
    total_calories_per_group = []
    for group in groups:
        total_calories = 0
        for calorie in group:
            total_calories += int(calorie)
        total_calories_per_group.append(total_calories)
    return total_calories_per_group


def get_top_three_groups(total_calories_per_group):
    top_three_groups = []
    for i in range(3):
        top_three_groups.append(max(total_calories_per_group))
        total_calories_per_group.remove(max(total_calories_per_group))
    return top_three_groups


def sum_top_three_groups(top_three_groups):
    total_calories = 0
    for group in top_three_groups:
        total_calories += group
    return total_calories


print(sum_top_three_groups(get_top_three_groups(sum_each_group(group_input(open_input_file())))))