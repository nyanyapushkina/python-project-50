#!/usr/bin/env python3
import argparse
from gendiff.scripts import generate_diff

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',  dest='format', help='set format of output')
args = parser.parse_args()
print(args)

def main():
    generate_diff(filepath1, filepath2)


if __name__ == '__main__':
    main()