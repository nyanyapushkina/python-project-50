import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path

def test_stylish_json():
    path_dict1 = get_fixture_path('file1.json')
    path_dict2 = get_fixture_path('file2.json')
    path_result = get_fixture_path('stylish_result.txt')

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, 'stylish') == expected_output

def test_stylish_yml():
    path_dict1 = get_fixture_path('file1.yml')
    path_dict2 = get_fixture_path('file2.yml')
    path_result = get_fixture_path('stylish_result.txt')

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, 'stylish') == expected_output

def test_plain_json():
    path_dict1 = get_fixture_path('file1.json')
    path_dict2 = get_fixture_path('file2.json')
    path_result = get_fixture_path('plain_result.txt')

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, 'plain') == expected_output

def test_plain_yml():
    path_dict1 = get_fixture_path('file1.yml')
    path_dict2 = get_fixture_path('file2.yml')
    path_result = get_fixture_path('plain_result.txt')

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, 'plain') == expected_output

def test_json():
    path_dict1 = get_fixture_path('file1.json')
    path_dict2 = get_fixture_path('file2.json')
    path_result = get_fixture_path('json_result.json')

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, 'json') == expected_output

def test_yml():
    path_dict1 = get_fixture_path('file1.yml')
    path_dict2 = get_fixture_path('file2.yml')
    path_result = get_fixture_path('json_result.json')

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, 'json') == expected_output

def get_fixture_path(file_name):
    return Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)
