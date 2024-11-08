def stylish(diff_list):
    return gendiff_output(diff_list)


def format_value(value, indent):
    """Process data to get a required result"""
    if isinstance(value, dict):
        indent += '    '
        result = format_dict(value, indent)
        return result
    elif value is False:
        return 'false'
    elif value is True:
        return 'true'
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_dict(dict, indent):
    result = '{\n'
    for key in dict.keys():
        value = format_value(dict[key], indent)
        result += f"{indent}  {key}: {value}\n"
    result += indent[:-2] + '}'
    return result


def gendiff_output(diff_list, level=0):  # noqa: C901
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    diff_list.sort(key=lambda x: x['name'])
    for node in diff_list:
        if node['status'] == 'nested':
            children_output = gendiff_output(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {children_output}\n"
        if node['status'] == 'not changed':
            data = format_value(node['data'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        elif node['status'] == 'added':
            data = format_value(node['data'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        elif node['status'] == 'deleted':
            data = format_value(node['data'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        elif node['status'] == 'changed':
            data_before = format_value(node['data before'], indent)
            data_after = format_value(node['data after'], indent)
            result += (f"{indent}- {node['name']}: {data_before}\n"
                       f"{indent}+ {node['name']}: {data_after}\n")
    result += indent[:-2] + '}'
    return result
