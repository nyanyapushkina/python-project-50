#!/usr/bin/env python3 

from gendiff.generate_diff import generate_diff
from gendiff.read_files.argparse import parser_arg

def main():
    first_file, second_file, output_format = parser_arg()
    result = generate_diff(first_file, second_file, output_format)
    print(result)

if __name__ == '__main__':
    main()
