class Voxel():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.pos = (x, y, z)
        self.neighbors = []
        self.possible_neighbors = set()
        self.exposed = 6
        self.find_possible_neighbors()

    def find_possible_neighbors(self):
        self.possible_neighbors.add((self.x-1, self.y, self.z))
        self.possible_neighbors.add((self.x+1, self.y, self.z))
        self.possible_neighbors.add((self.x, self.y-1, self.z))
        self.possible_neighbors.add((self.x, self.y+1, self.z))
        self.possible_neighbors.add((self.x, self.y, self.z-1))
        self.possible_neighbors.add((self.x, self.y, self.z+1))

    def find_neighbors(self, voxels):
        for v in voxels:
            if v.pos in self.possible_neighbors:
                #print(self.x, self.y, self.z)
                #print(v.x, v.y, v.z)
                self.neighbors.append(v)
                self.exposed-=1



if __name__ == "__main__":
    with open("./day18/test_input.txt", "r") as f:
        data = f.read().splitlines()
    voxels = []
    for item in data:
        x,y,z = map(int, item.split(","))
        voxels.append(Voxel(x,y,z))
    for voxel in voxels:
        voxel.find_neighbors(voxels)
    exposed_sides=0
    for voxel in voxels:
        exposed_sides+=voxel.exposed
    print(exposed_sides)
    #TODO: include flood fill
