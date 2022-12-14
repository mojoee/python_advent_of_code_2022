def is_interesting(x):
    interesting_values = [20, 60, 100, 140, 180, 220]
    if x in interesting_values:
        return True
    else:
        return False


def calculate_signal_strength(x, cycle):
    return x*cycle


def draw_sprite(cycle, x):
    if cycle - 1 <= x <= cycle+1:
        #print("#", end="")
        print("\u2588", end="")
    else:
        print(".", end="")
    if cycle % 40 == 0:
        print()
        cycle -= 40
    return cycle


if __name__ == "__main__":
    with open("./day10/input.txt", "r") as f:
        data = f.read().splitlines()
    print(data)
    x = 1
    cycle = 0
    sum = 0
    for item in data:
        # print(item)
        cycle += 1
        cycle=draw_sprite(cycle, x)
        
        if is_interesting(cycle):
            sum += calculate_signal_strength(cycle, x)
        if item.startswith("addx"):
            increase = int(item.split(" ")[-1])
            cycle += 1
            x += increase
            cycle = draw_sprite(cycle, x)

        if is_interesting(cycle) and not item.startswith("noop"):
            sum += calculate_signal_strength(cycle, x)
    print(sum)