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
            item = self.operation(item)
            if item % self.divisor == 0:
                self.true_monkey.receive(item)
            else:
                self.false_monkey.receive(item)
            self.processed_items +=1

    def receive_item(self, item):
        self.items.append(item)

    def assign_partner(self, all_monkeys):
        self.true_monkey = all_monkeys[self.true_monkey]
        self.false_monkey = all_monkeys[self.false_monkey]

def data_to_dict(data):
    output = dict()
    output["id"]=item[0][-2]
    items = item[1].split(":")[1].split(",")
    items = [int(x.replace(" ", "")) for x in items]
    output["items"] = items
    output["number"] = data[2].split(": ")[1][-1]
    output["operation"] = ops[data[2].split(": ")[1][-3]]
    output["divisor"] = int(data[3][-1])
    output["tm"] = int(data[4][-1])
    output["fm"] = int(data[5][-1])

    return output




def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


if __name__ == "__main__":
    with open("./day11/input.txt", "r") as f:
        data = f.read().splitlines()
    monkeys = []
    for item in chunker(data, 7):
        dic1 = data_to_dict(item)
        monkeys.append(Monkey(dic1))

    # assign monkeys to their true and false partners
    for m in monkeys:
        m.assign_partner(monkeys)

    for i in range(20):
        for m in monkeys:
            m.process_items()
    
    print(f"score: {score}")

