import argparse
import json
import os
import yaml


def open_file(filepath1, filepath2):
    file1name, file1_extension = os.path.splitext(filepath1)
    file2name, file2_extension = os.path.splitext(filepath2)
    if file2_extension == '.json':
        file1 = json.load(open(filepath1))
        file2 = json.load(open(filepath2))
    if file2_extension == '.yml' or file2_extension == '.yaml':
        with open(filepath1, 'r') as f:
            file1 = yaml.load(f, Loader=yaml.SafeLoader)
        with open(filepath2, 'r') as f:
            file2 = yaml.load(f, Loader=yaml.SafeLoader)
    else:
        print('File type is not supported')
    
    return file1, file2