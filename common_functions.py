#!/usr/bin/env python
# coding: utf-8
import re
import os
import shutil
import sys
from collections import defaultdict

def tree_built_preview(results,output_path):
    tree=defaultdict(list)
    for result in results:
        folder=result["folder_name"]
        ext=os.path.splitext(result["path"].lower())[1]
        file = f"{result['file_name']}{ext}"
        tree[folder].append(file)

    lines=[f"{output_path}"]
    for folder in sorted(tree):
        lines.append(f"├── {folder}/")
        for i, file in enumerate(sorted(tree[folder])):
            prefix = "│   └──" if i == len(tree[folder]) - 1 else "│   ├──"
            lines.append(f"{prefix} {file}")

    return "\n".join(lines)

def organise(results,output_path):
    os.makedirs(output_path, exist_ok=True)
    for entry in results:
        path=entry["path"]
        folder=entry["folder_name"]
        ext=os.path.splitext(entry["path"].lower())[1]
        file = f"{entry['file_name']}{ext}"
        dest_folder=os.path.join(output_path,folder)
        os.makedirs(dest_folder,exist_ok=True)
        dest_path=os.path.join(dest_folder,file)
        shutil.move(path,dest_path)

    return None

def suppress_stderr(func):
    def wrapper(*args, **kwargs):
        original_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')
        try:
            return func(*args, **kwargs)
        finally:
            sys.stderr.close()
            sys.stderr = original_stderr
    return wrapper
