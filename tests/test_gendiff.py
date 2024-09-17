from gendiff.generate_diff import generate_diff
from pathlib import Path

def test_diff_json_stylish():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_output = read_file(get_fixture_path('stylish_result.txt'))
    
    assert generate_diff(file1, file2, 'stylish') == expected_output

def test_diff_yml_stylish():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected_output = read_file(get_fixture_path('stylish_result.txt'))
    
    assert generate_diff(file1, file2, 'stylish') == expected_output

def test_diff_json_plain():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_output = read_file(get_fixture_path('plain_result.txt'))
    
    assert generate_diff(file1, file2, 'plain') == expected_output

def test_diff_yml_plain():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected_output = read_file(get_fixture_path('plain_result.txt'))
    
    assert generate_diff(file1, file2, 'plain') == expected_output

def test_diff_json_json_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_output = read_file(get_fixture_path('json_result.json'))
    
    assert generate_diff(file1, file2, 'json') == expected_output

def test_diff_yml_json_format():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected_output = read_file(get_fixture_path('json_result.json'))
    
    assert generate_diff(file1, file2, 'json') == expected_output

def get_fixture_path(file_name):
    return Path(__file__).parent / 'fixtures' / file_name

def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip()  
