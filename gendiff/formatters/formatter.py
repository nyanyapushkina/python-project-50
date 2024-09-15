from gendiff.formatters import stylish, plain, json_format

def format_diff(list_diff, format_name="stylish"):
    if format_name == 'stylish':
        return stylish(list_diff)
    elif format_name == 'plain':
        return plain(list_diff)
    elif format_name == 'json':
        return json_format(list_diff)
    
    raise ValueError('Unknown format. Only stylish, plain and json are supported.')