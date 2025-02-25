def extract_value(line):
    first_digit = None
    last_digit = None
    
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0

def sum(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        value = extract_value(line.strip())
        print(f"Value in line '{line.strip()}' is: {value}")
        total_sum += value
    
    return total_sum

filename = 'input_3.txt'
total_sum = sum(filename)
print(f"Total sum is: {total_sum}")
