class Position():
    def __init__(self, x, y, pos) -> None:
        self.x = x
        self.y = y
        self.visited_position = set()
        self.tail = pos

    def move_horizontal(self, x, sod):
        for i in range(x):
            self.move_horizontal_step(sod)
            self.add_current_position()

    def move_vertical(self, y, sod):
        for i in range(y):
            self.move_vertical_step(sod)
            self.add_current_position()
            self.tail.follow_position(self.x, self.y)
    
    def add_current_position(self):
        self.visited_position.add((self.x, self.y))

    def move_horizontal_step(self, sod):
        self.x += sod * 1
    
    def move_vertical_step(self, sod):
        self.y += sod * 1

    def follow_position(self, x, y):
        self.tail.x = x
        self.tail.y = y
        self.add_current_position()


if __name__ == "__main__":
    with open("./day9/test_input.txt", "r") as f:
        data = f.read().splitlines()
    t = Position(0, 0, None)
    h = Position(0, 0, t)
    visited_positions = set()
    for move in data:
        direction, length = move.split(" ")
        length = int(length)
        if direction == "R":
            h.move_horizontal(length, 1)
        elif direction == "L":
            h.move_horizontal(length, -1)
        elif direction == "U":
            h.move_vertical(length, 1)
        elif direction == "D":
            h.move_vertical(length, -1)
    print(len(t.visited_position))
    print(t.visited_position)
