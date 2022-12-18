import numpy as np

class Position():
    def __init__(self, x, y, pos) -> None:
        self.x = x
        self.y = y
        self.visited_position = set()
        self.tail = pos
        self.add_current_position()

    def move_horizontal(self, x, sod):
        for i in range(x):
            self.move_horizontal_step(sod)
            self.add_current_position()
            if are_touching(self, self.tail):
                continue
            self.follow_position(sod)

    def move_vertical(self, y, sod):
        for i in range(y):
            self.move_vertical_step(sod)
            self.add_current_position()
            if are_touching(self, self.tail):
                continue
            self.follow_position(sod)

    def add_current_position(self):
        self.visited_position.add((self.x, self.y))

    def move_horizontal_step(self, sod):
        self.x += sod * 1

    def move_vertical_step(self, sod):
        self.y += sod * 1

    def follow_position(self, sod):
        if self.x == self.tail.x:
            self.tail.y += sod*1
        elif self.y == self.tail.y:
            self.tail.x += sod*1
        else:
            if (self.x - self.tail.x) < 0 and (self.y - self.tail.y) < 0:
                self.tail.x -= 1
                self.tail.y -= 1
            if (self.x - self.tail.x) > 0 and (self.y - self.tail.y) < 0:
                self.tail.x += 1
                self.tail.y -= 1
            if (self.x - self.tail.x) < 0 and (self.y - self.tail.y) > 0:
                self.tail.x -= 1
                self.tail.y += 1
            if (self.x - self.tail.x) > 0 and (self.y - self.tail.y) > 0:
                self.tail.x += 1
                self.tail.y += 1
        self.tail.add_current_position()
        if self.tail.tail == None:
            return
        self.tail.tail.follow_position(sod)


def are_touching(pos1, pos2):
    if pos1.x == pos2.x and pos1.y == pos2.y:
        return True
    if pos1.x == pos2.x and (abs(pos1.y-pos2.y) <= 1):
        return True
    if pos1.y == pos2.y and (abs(pos1.x-pos2.x) <= 1):
        return True
    if (abs(pos1.x-pos2.x)) == 1 and (abs(pos1.y-pos2.y) == 1):
        return True
    else:
        return False

if __name__ == "__main__":
    with open("./day9/test_input.txt", "r") as f:
        data = f.read().splitlines()

    t9 = Position(0, 0, None)
    t8 = Position(0, 0, t9)
    t7 = Position(0, 0, t8)
    t6 = Position(0, 0, t7)
    t5 = Position(0, 0, t6)
    t4 = Position(0, 0, t5)
    t3 = Position(0, 0, t4)
    t2 = Position(0, 0, t3)
    t1 = Position(0, 0, t2)
    h = Position(0, 0, t1)
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
    print(len(t5.visited_position))
    #print(t.visited_position)

    # vis = np.zeros((6, 6), dtype=int)
    # for pos in t.visited_position:
    #     vis[pos[0], pos[1]]= 1
    # print(vis)