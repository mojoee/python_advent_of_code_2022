def find_marker(sequence: str):
    sequence_length = 14
    counter = sequence_length
    start_item = sequence[:counter]
    not_found = True
    for letter in sequence[sequence_length:]:
        if check_unique(start_item):
            print(f"Sequence found: {start_item}")
            return counter
        start_item = start_item[1:] + letter
        counter += 1

    return None


def check_unique(seq: str):
    a = len(seq)
    b = len(list(set(seq)))
    if a == b:
        return True
    else:
        return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    for item in data:
        answer = find_marker(item)
    print(f"Answer: {answer}")
