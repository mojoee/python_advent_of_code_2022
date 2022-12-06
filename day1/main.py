if __name__ == "__main__":
    with open("input.txt", "r") as myfile:
        data = myfile.read().splitlines()
    maximum_value = 0
    current_value = 0
    values = []
    for line in data:
        if line == "":
            values.append(current_value)
            current_value = 0
        else:
            current_value += int(line)
    values = sorted(values, reverse=True)
    sum_top_3 = sum(values[:3])
    print(f"Max: {sum_top_3}")
