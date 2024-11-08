import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path

@pytest.mark.parametrize("file1, file2, result_file, format", [
    ('file1.json', 'file2.json', 'stylish_result.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'stylish_result.txt', 'stylish'),
    ('file1.json', 'file2.json', 'plain_result.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'plain_result.txt', 'plain'),
    ('file1.json', 'file2.json', 'json_result.json', 'json'),
    ('file1.yml', 'file2.yml', 'json_result.json', 'json')
])
def test_generate_diff(file1, file2, result_file, format):
    path_dict1 = get_fixture_path(file1)
    path_dict2 = get_fixture_path(file2)
    path_result = get_fixture_path(result_file)

    with open(path_result) as f:
        expected_output = f.read().strip()

    assert generate_diff(path_dict1, path_dict2, format) == expected_output


def get_fixture_path(file_name):
    return Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)
