def safe_report(levels):
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    if not (increasing or decreasing):
        return False

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if not (1 <= diff <= 3):
            return False

    return True

def check_file(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()

    for report in reports:
        levels = list(map(int, report.strip().split()))
        if safe_report(levels):
            print(f"Report {levels} Safe")
        else:
            print(f"Report {levels} Unsafe")

filename = 'input_2.txt'
check_file(filename)
