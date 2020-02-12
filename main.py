import argparse

from src.ascify import Ascify
from src.file import File


def main():
    # Arguments
    parser = argparse.ArgumentParser(description="A commandline utility to generate HTML animations from images")
    parser.add_argument("file", help="specify input file")
    arguments = parser.parse_args()

    # Handle file
    File(arguments.file)

    # Generate Juice
    Ascify(File.open())


if __name__ == "__main__":
    main()
