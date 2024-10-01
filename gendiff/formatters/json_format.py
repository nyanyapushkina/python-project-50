import json


def json_format(diff_list):
    json_result = json.dumps(diff_list, indent=4)
    return json_result
