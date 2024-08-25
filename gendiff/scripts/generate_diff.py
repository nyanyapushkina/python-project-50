import json

def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    intersection = {x:file1[x] for x in file1 
                              if x in file2}
    # Тут я планирую как-то определить, какие появились ноые ключи, а какие пропали.
    # Затем – сравнить изменились ли значения у ключей
    # Затем сформировать новые словарь и отсортировать по ключам
    # Преобразовать в строку (как-то добавить знаки?.... )
    return result
