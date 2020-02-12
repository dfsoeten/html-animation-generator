import json
from collections import Iterable


class Ascify:
    WIDTH = 40

    ASCII_CHARS = ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']
    ASCII_CHARS = ASCII_CHARS[::-1]

    generator = None

    results = None

    @classmethod
    def __init__(cls, generator):
        cls.generator = generator

        cls.generate()
        cls.print()
        cls.save()

    @classmethod
    def generate(cls):
        cls.results = []

        for frames in cls.generator:
            if not isinstance(frames, Iterable):
                frame = cls.grayscalify(cls.resize(frames))
                pixels = cls.modify(frame)

                cls.results.append('\n'.join([pixels[index:index + cls.WIDTH] for index in range(0, len(pixels), cls.WIDTH)]))
            else:
                for frame in frames:
                    frame = cls.grayscalify(cls.resize(frame))
                    pixels = cls.modify(frame)

                    cls.results.append('\n'.join([pixels[index:index + cls.WIDTH] for index in range(0, len(pixels), cls.WIDTH)]))

        return cls.results

    @classmethod
    def resize(cls, image):
        (old_width, old_height) = image.size

        return image.resize((cls.WIDTH, int((float(old_height) / float(old_width)) * cls.WIDTH)))

    @classmethod
    def grayscalify(cls, image):
        return image.convert('L')

    @classmethod
    def modify(cls, image, buckets=25):
        return ''.join([cls.ASCII_CHARS[pixel_value // buckets] for pixel_value in list(image.getdata())])

    @classmethod
    def print(cls):
        if len(cls.results) == 1:
            print(cls.results[0])

        else:
            for frame in cls.results:
                print(frame + "\n")

    @classmethod
    def save(cls):
        with open('source.js', 'r') as source, open('index.js', 'w') as index:
            index.write("let data = " + json.dumps({'frames': list(cls.results)}) + "\n")
            index.write(source.read())
