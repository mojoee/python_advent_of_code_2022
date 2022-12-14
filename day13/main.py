
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def convert_str_list(str: str):
    print(str)
    str=str[1:-1]
    list = [int(x) for x in str.split(",")]
    return list
    

if __name__ == "__main__":
    print("starting")
    with open("./day13/input.txt") as f:
        data = f.read().splitlines()
    total = 0
    
    for n, item in enumerate(chunker(data,3)):
        right_order = True
        convert_str_list(item[0])
        for i, j in zip(item[0], item[1]):
            if i > j:
                print(f"issue {i} {j}")
                right_order = False
        if right_order:
            total+=n
    print(n)

