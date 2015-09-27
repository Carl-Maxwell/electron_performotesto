from loremipsum import get_paragraph
from names      import get_last_name
from os         import mkdir, utime
from os.path    import exists
from random     import choice, random
import sys

class Generator:
    def __init__(self, base = "./"):
        if base[-1] == "/":
            base = base[0:-1]

        self.files   = []
        self.folders = [base]

        while len(self.files) < 100:
            self.generate()
        self.files.sort()

        wordcount = 0
        while wordcount < 100000:
            wordcount += self.fill()

    def name(self, path):
        return path + "/" + get_last_name().lower()

    def isFileBad(self, file):
        return file in self.files or file in self.folders or exists(file)

    def touch(self, file):
        if self.isFileBad(file):
            return

        self.files.append(file)
        open(file, 'w')

    def mkdir(self, file):
        if self.isFileBad(file):
            return

        self.folders.append(file)
        mkdir(file)

    def generate(self):
        path = choice(self.folders)

        self.touch(self.name(path))
        self.mkdir(self.name(path))

    def fill(self):
        paragraphs = ''

        for i in range(1 + int(random()*5)):
            paragraphs += get_paragraph() + " \n"

        file = open(choice(self.files), 'a+')
        file.write(paragraphs)
        file.close()

        return len(paragraphs.split(' '))


def main(base = "./"):
    g = Generator(base)
    g.files.sort
    print("\n".join(g.files))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
