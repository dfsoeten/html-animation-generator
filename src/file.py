import copy
import os
import re
import sys
from PIL import Image


class File:
    path = ''

    extension = ''

    @classmethod
    def __init__(cls, path):
        cls.path = path
        cls.extension = os.path.splitext(path)[1]

        if not os.path.isfile(path):
            sys.stderr.write("File " + cls.path + " not found\n")
            exit(1)

    @classmethod
    def open(cls):
        if cls.extension == ".gif":
            yield cls.gif()

        if re.compile("^.jpg|.jpeg|.png$").match(cls.extension):
            yield cls.img()

    @classmethod
    def img(cls):
        return Image.open(cls.path)

    @classmethod
    def gif(cls):
        results = []

        image = Image.open(cls.path)

        try:
            while 1:
                image.seek(image.tell() + 1)
                results.append(copy.copy(image))

        except EOFError:
            pass

        return results


