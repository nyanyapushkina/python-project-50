def diff(dict1, dict2):
    result = []
    all_keys = set(dict1.keys()).union(set(dict2.keys()))
    
    for key in sorted(all_keys):
        if key not in dict1:
            result.append({
                'name': key,
                'status': 'added',
                'data': dict2[key]
                })
        elif key not in dict2:
            result.append({
                'name': key,
                'status': 'deleted',
                'data': dict1[key]
                })
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result.append({
                'name': key,
                'status': 'nested',
                'children': diff(dict1[key], dict2[key])
                })
        elif dict1[key] == dict2[key]:
            result.append({
                'name': key,
                'status': 'not changed',
                'data': dict1[key]
                })
        else:
            result.append({
                'name': key,
                'status': 'changed',
                'data before': dict1[key],
                'data after': dict2[key]
                })
            
        return result