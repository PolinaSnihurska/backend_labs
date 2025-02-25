def calculate_total_distance(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))

    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)

    return total_distance

filename = 'input_1.txt'

total_distance = calculate_total_distance(filename)
print("Total distance:", total_distance)
