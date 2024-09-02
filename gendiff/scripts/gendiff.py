#!/usr/bin/env python3
import argparse
import json


def gendiff(filepath1, filepath2):
    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))
    all_keys = set(file1.keys()).union(set(file2.keys()))
    result = []

    for key in sorted(all_keys):
        if key in file1 and key not in file2:
            result.append(f"  - {key}: {file1[key]}")
        elif key in file2 and key not in file1:
            result.append(f"  + {key}: {file2[key]}")
        elif file1[key] != file2[key]:
            result.append(f"  - {key}: {file1[key]}")
            result.append(f"  + {key}: {file2[key]}")
        else:
            result.append(f"    {key}: {file1[key]}")

    result_line = "\n".join(result)
    return f"{{\n{result_line}\n}}"


def main():
    parser = argparse.ArgumentParser(
        description=(
            'Compares two configuration files '
            'and shows a difference.'
        )
    )    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
                        dest='format', 
                        help='set format of output')
    args = parser.parse_args()

    diff_result = gendiff(args.first_file, args.second_file)
    print(diff_result)


if __name__ == '__main__':
    main()
