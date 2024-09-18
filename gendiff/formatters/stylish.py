def stylish(diff_list):
    return generate_diff_output(diff_list)


def calculate_indentation(depth):
    return '  ' + '    ' * depth


def format_value(value, indent):
    if isinstance(value, dict):
        return format_dict(value, indent)
    elif value is False:
        return 'false'
    elif value is True:
        return 'true'
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_dict(data, indent):
    result = '{\n'
    for key in data.keys():
        value = format_value(data[key], indent + '    ')
        result += f"{indent}  {key}: {value}\n"
    result += indent[:-2] + '}'
    return result


def process_node(node, level):
    indent = calculate_indentation(level)
    
    if node['status'] == 'nested':
        children_output = generate_diff_output(node['children'], level + 1)
        return f"{indent}  {node['name']}: {children_output}\n"
    
    if node['status'] == 'not changed':
        data = format_value(node['data'], indent)
        return f"{indent}  {node['name']}: {data}\n"
    elif node['status'] == 'added':
        data = format_value(node['data'], indent)
        return f"{indent}+ {node['name']}: {data}\n"
    elif node['status'] == 'deleted':
        data = format_value(node['data'], indent)
        return f"{indent}- {node['name']}: {data}\n"
    elif node['status'] == 'changed':
        data_before = format_value(node['data before'], indent)
        data_after = format_value(node['data after'], indent)
        return (f"{indent}- {node['name']}: {data_before}\n"
                f"{indent}+ {node['name']}: {data_after}\n")


def generate_diff_output(diff_list, level=0):
    result = '{\n'
    diff_list.sort(key=lambda x: x['name'])

    for node in diff_list:
        result += process_node(node, level)

    result += calculate_indentation(level) + '}'
    return result
