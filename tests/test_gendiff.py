import json
import os
from gendiff.scripts.gendiff import gendiff

def test_gendiff():
    file1_path = os.path.join('tests', 'file1.json')
    file2_path = os.path.join('tests', 'file2.json')
    correct_result = "{\n  - follow: False\n  - proxy: 123.234.53.22\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}"
    assert gendiff(file1_path, file2_path) == correct_result
