import operator

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul}

class Monkey():
    def __init__(self, dict) -> None:
        self.id = dict["id"]
        self.items = dict["items"]
        self.operation = dict["operation"]
        self.number = dict["number"]
        self.divisor = dict["divisor"]
        self.true_monkey = dict["tm"]
        self.false_monkey = dict["fm"]
        self.processed_items = 0

    def process_items(self):
        for item in self.items:
            if self.number == "square":
                item = self.operation(item, item)
            else:
                item = self.operation(item, int(self.number))
            if round2:
                item = item % monkeymod
            else:
                item = item // 3

            if item % self.divisor == 0:
                self.true_monkey.receive_item(item)
            else:
                self.false_monkey.receive_item(item)
            self.processed_items += 1
        self.items = []

    def receive_item(self, item):
        self.items.append(item)

    def assign_partner(self, all_monkeys):
        self.true_monkey = all_monkeys[self.true_monkey]
        self.false_monkey = all_monkeys[self.false_monkey]

    def show_items(self):
        print(f"Monkey {self.id}")
        for item in self.items:
            print(f"{item}", end=" ")

def data_to_dict(data):
    output = dict()
    output["id"] = item[0][-2]
    items = item[1].split(":")[1].split(",")
    items = [int(x.replace(" ", "")) for x in items]
    output["items"] = items
    output["number"] = data[2].split(": ")[1][-2:]
    if data[2].endswith("old"):
        output["operation"] = ops[data[2].split(": ")[1][-5]]
        output["number"] = "square"
    else:
        if data[2].split(": ")[1][-3] == " ":
            output["operation"] = ops[data[2].split(": ")[1][-4]]
        else:
            output["operation"] = ops[data[2].split(": ")[1][-3]]
    output["divisor"] = int(data[3][-2:])
    output["tm"] = int(data[4][-1])
    output["fm"] = int(data[5][-1])

    return output




def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


if __name__ == "__main__":
    with open("./day11/input.txt", "r") as f:
        data = f.read().splitlines()
    monkeys = []
    monkeymod = 1
    for item in chunker(data, 7):
        dic1 = data_to_dict(item)
        monkeys.append(Monkey(dic1))
        monkeymod *= int(dic1["divisor"])

    # assign monkeys to their true and false partners
    for m in monkeys:
        m.assign_partner(monkeys)

    round2 = True
    if round2:
        n = 10000
    else:
        n = 20
    for i in range(n):
        for m in monkeys:
            m.process_items()
        #for m in monkeys:
        #    m.show_items()
    monkey_stuff = sorted([x.processed_items for x in monkeys], reverse=True)
    print(f"score: {monkey_stuff[0]*monkey_stuff[1]}")

