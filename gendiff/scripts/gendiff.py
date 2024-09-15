#!/usr/bin/env python3 

from gendiff import generate_diff
from gendiff.read_files.argparse import parser_arg

def main():
    first_file, second_file, output_format = parser_arg()
    print(generate_diff(first_file, second_file, output_format))

if __name__ == '__main__':
    main()
