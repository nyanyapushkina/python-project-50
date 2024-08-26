from gendiff.scripts.gendiff import gendiff

def test_gendiff():
    file1 = json.load(open('file1.json'))
    file2 = json.load(open('file2.json'))
    assert gendiff(file1, file2) == "{\n- follow: false\nhost: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}"
