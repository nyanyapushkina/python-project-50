
from gendiff.formatters.formatter import format_diff
from gendiff.read_files.parser import open_file
from gendiff.scripts.diff import diff


def generate_diff(path_file1: str,
                  path_file2: str,
                  format_name: str = 'stylish') -> tuple:
    dict1 = open_file(path_file1)
    dict2 = open_file(path_file2)
    list_diff = diff(dict1, dict2)
    return format_diff(list_diff, format_name)
