from names import get_last_name
from random import random, choice
from os import utime, mkdir

class Generator:
    def __init__(self):
        self.files = []
        self.folders = ["./"]

        while len(self.folders) < 100:
            self.generate()
        self.files.sort()
        self.files = map(lambda x: x.replace('//', '/'), self.files)

    def name(self, path):
        return path + "/" + get_last_name().lower()

    def isFileBad(self, file):
        return file in self.files or file in self.folders

    def touch(self, file):
        if self.isFileBad(file):
            return

        self.files.append(file)
        # utime(name)

    def mkdir(self, file):
        if self.isFileBad(file):
            return

        self.folders.append(file)
        # mkdir(name)

    def generate(self):
        path = choice(self.folders)

        self.touch(self.name(path))
        self.mkdir(self.name(path))

def main():
    g = Generator()
    g.files.sort
    print("\n".join(g.files))

if __name__ == "__main__":
    main()
