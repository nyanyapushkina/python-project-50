import yaml
from yaml.loader import SafeLoader
import os
from gendiff.scripts.gendiff import gendiff

def test_gendiff():
    file1_path = os.path.join('tests', 'fixtures/file1.yaml')
    file2_path = os.path.join('tests', 'fixtures/file2.yaml')
    correct_result = "{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"
    assert gendiff(file1_path, file2_path) == correct_result 