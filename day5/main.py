import re

class Stack:
    def __init__(self):
        self.items = []

    # items check the None:
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    # item append:
    def push(self, item):
        self.items.append(item)

    # item delete or pop:
    def delete(self):
        return self.items.pop()

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def perform_move(command):
    numbers = [int(x) for x in re.findall(r'\d+', command)]
    start = stacks_container[numbers[1]-1] 
    end = stacks_container[numbers[2]-1] 
    for i in range(numbers[0]):
        #end.push(start.items[-numbers[0]:])
        end.push(start.items[-1])
        start.delete()
    #for i in range(numbers[0]):



if __name__ == "__main__":
    with open("./day5/input.txt", "r") as f:
        data = f.read().splitlines()
    # print(data)
    n_stacks = 9
    stacks_container = []
    for i in range(n_stacks):
        stacks_container.append(Stack())
    length_crate = (len(data[0])+1)/9

    for it in data[:10]:
        for i in range(9):
            box = it[i*4:i*4+3]
            if  box == "   ":
                print("empty")
            elif has_numbers(box):
                continue
            elif box =='':
                continue
            else:
                stacks_container[i].push(box)
        print(it)
        if it == "":
            print("operations start")
            print("current stacks: ")
            for st in stacks_container:
                print(st.items)
    for st in stacks_container:
        st.items = st.items[::-1]
    for it in data[10:]:
        perform_move(it)
    
    for st in stacks_container:
        print(st.items[-1])