import json
import yaml
from pathlib import Path


def open_file(filepath):
    """Parse files and check if they're in acceptable format"""
    file_extension = Path(filepath).suffix
    if file_extension.lower() == '.json':
        with open(filepath) as f:
            return json.load(f)
    elif file_extension.lower() in ['.yaml', '.yml']:
        with open(filepath) as f:
            return yaml.safe_load(f)
    raise ValueError("Unsupported file format")
