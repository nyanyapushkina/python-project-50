def plain(diff_list):
    return generate_diff_output(diff_list)


def generate_diff_output(diff_list):
    diff_list.sort(key=lambda x: x['name'])
    result = get_diff_plain_list(diff_list)
    return '\n'.join(result)


def format_value(data):
    """Process data to get a required result"""
    if isinstance(data, (dict, list)):
        result = '[complex value]'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    elif isinstance(data, str):
        result = "'{}'".format(data)
    else:
        result = '{}'.format(data)
    return result


def get_diff_plain_list(diff_list, path=''):
    """Process each node to define its status"""
    result = []
    for node in diff_list:
        if node['status'] == 'nested':
            path_to_change = f"{path}{node['name']}."
            difference = get_diff_plain_list(node['children'], path_to_change)
            result.extend(difference)
        if node['status'] == 'added':
            path_to_change = f"{path}{node['name']}"
            change = format_value(node['data'])
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['status'] == 'deleted':
            path_to_change = f"{path}{node['name']}"
            change = format_value(node['data'])
            difference = f"Property '{path_to_change}' was removed"
            result.append(difference)
        if node['status'] == 'changed':
            path_to_change = f"{path}{node['name']}"
            change_before = format_value(node['data before'])
            change_after = format_value(node['data after'])
            difference = (
                f"Property '{path_to_change}' was updated. "
                f"From {change_before} to {change_after}"
            )
            result.append(difference)
    return result
