def parse_filesystem(input_data):
    filesystem = {}
    current_path = '/'
    filesystem[current_path] = {}

    for line in input_data.splitlines():
        if line.startswith('$ cd'):
            parts = line.split()
            if parts[2] == '/':
                current_path = '/'
            elif parts[2] == '..':
                current_path = '/'.join(current_path.split('/')[:-1])
            else:
                current_path = f"{current_path}/{parts[2]}".replace('//', '/')
                filesystem[current_path] = {}
        elif line.startswith('$ ls'):
            pass
        else:
            parts = line.split()
            name = parts[1]
            if parts[0] == 'dir':
                filesystem[current_path][name] = 'dir'
            else:
                size = int(parts[0])
                filesystem[current_path][name] = size

    return filesystem

def calculate_directory_size(filesystem, path):
    size = 0
    for item, value in filesystem.get(path, {}).items():
        if value == 'dir':
            size += calculate_directory_size(filesystem, f"{path}/{item}".replace('//', '/'))
        else:
            size += value
    return size

def main():
    with open('input_4.txt', 'r') as file:
        input_data = file.read()

    filesystem = parse_filesystem(input_data)

    directory_sizes = {}
    for path in filesystem:
        directory_sizes[path] = calculate_directory_size(filesystem, path)

    total_size = sum(size for path, size in directory_sizes.items() if size <= 100000)
    print('Total size of directories with size <= 100000:', total_size)

if __name__ == '__main__':
    main()
