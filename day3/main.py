def find_priority(letter):
    values = "abcdefghijklmnopqrstuvwxyz"
    p = values.find(letter.lower()) + 1
    if letter.isupper():
        p += 26
    return p


def find_duplicate_letter(item):
    n = int(len(item)/2)
    l1 = item[:n]
    l2 = item[n:]
    for letter in l1:
        if letter in l2:
            return letter


def find_badge(item):
    letters_1_2 = set()
    for letter in item[0]:
        if letter in item[1]:
            letters_1_2.add(letter)
    for letter in item[2]:
        if letter in letters_1_2:
            return letter
    return None



if __name__ == "__main__":
    with open("input.txt", "r") as myfile:
        data = myfile.read().splitlines()
    print(data)
    score = 0
    group = []
    for item in data:
        group.append(item)
        if len(group) > 2:
            duplicate = find_badge(group)
            group = []
            priority = find_priority(duplicate)
            score += priority
    print(f"final score: {score}")
