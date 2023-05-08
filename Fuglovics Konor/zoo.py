class Zoo:
    def __init__(self, plants, animals):
        self.plants = plants
        self.animals = animals

    def write(self):
        print(f"Plants: {self.plants}")
        print(f"Animals: {self.animals}")

    def write_file(self):
        with open('zoo.txt', 'w', encoding='utf-8') as file:
            file.write(f"Plants: {self.plants}\n")
            file.write(f"Animals: {self.animals}\n")


zoo = Zoo(100, 143)
zoo.write()
zoo.write_file()