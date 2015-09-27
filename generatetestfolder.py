import names
from random import random, choice
from os import utime, mkdir

class Generator:
    def __init__(self):
        self.files = []
        self.folders = ["./"]
        while len(self.folders) < 100:
            self.generate()
        self.files.sort
        self.files = map(lambda x: x.replace('//', '/'), self.files)

    def generate(self):
        path = choice(self.folders)
        name = names.get_last_name().lower()

        if random() < 0.75:
            # utime(path + name)
            self.files.append(path + "/" + name)
        else:
            # mkdir(name)
            self.folders.append(path + "/" + name)

def main():
    g = Generator()
    g.files.sort
    print("\n".join(g.files))

if __name__ == "__main__":
    main()
