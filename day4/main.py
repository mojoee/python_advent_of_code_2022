def convert_str_tuple(rows: str):
    a, b = rows.split(",")
    lb1, ub1 = map(int, a.split("-"))
    lb2, ub2 = map(int, b.split("-"))
    return lb1, ub1, lb2, ub2

def is_contained(tup):
    if tup[0] >= tup[2] and tup[1] <= tup[3]:
        return True
    elif tup[0] <= tup[2] and tup[1] >= tup[3]:
        return True
    else:
        return False


def does_overlap(tup):
    a = list(range(tup[0], tup[1]+1))
    b = list(range(tup[2], tup[3]+1))
    length_a_b = len(a) + len(b)
    a.extend(b)
    a_set = set(a)
    if len(list(a_set)) < length_a_b:
        return True
    else:
        return False

if __name__ == "__main__":
    with open("./day4/input.txt", "r") as f:
        data = f.read().splitlines()
    print(data)
    test = convert_str_tuple(data[0])
    count = 0
    for item in data:
        item = convert_str_tuple(item)
        if does_overlap(item):
            count += 1
    print(count)

