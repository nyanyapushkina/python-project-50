import json
import yaml
from pathlib import Path

def open_file(filepath):
    file_extension = Path(filepath).suffix
    if file_extension.lower() == '.json':
         with open(filepath) as f:
            return json.load(f)
    elif file_extension.lower() == '.yml' or file_extension.lower() == '.yaml':
        with open(filepath) as f:
            return yaml.safe_load(f)
