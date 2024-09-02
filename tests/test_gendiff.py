import json
import os
from gendiff.scripts.gendiff import gendiff

def normalize_output(output):
    return output.replace(' ', '').replace('\n', '').lower()
       

def test_gendiff():
    file1_path = os.path.join('tests', 'file1.json')
    file2_path = os.path.join('tests', 'file2.json')
    correct_result = "{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"
    assert normalize_output(gendiff(file1_path, file2_path)) == normalize_output(correct_result)
