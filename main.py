#!/usr/bin/env python
# coding: utf-8

import os
import sys
import warnings
import base64
import time
import re

# Reduce llama.cpp and Metal logs
os.environ["LLAMA_LOG_LEVEL"] = "ERROR"
os.environ["GGML_METAL_LOG_LEVEL"] = "NONE"

# Suppress Python warnings like PDF CropBox
warnings.filterwarnings("ignore", message="CropBox missing from /Page")


from text_processing import process_files_text
from tree_builder import tree_builder
from read_data import collect_file_path,read_file
from text_questioning import question
from common_functions import tree_built_preview,organise,suppress_stderr
from llama_cpp import Llama

# ------------------------
# Load models with clean logging
# ------------------------
@suppress_stderr
def load_llm_text():
    return Llama.from_pretrained(
        repo_id="MaziyarPanahi/Meta-Llama-3-8B-Instruct-GGUF",
        filename="Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
        n_ctx=4096,
        n_gpu_layers=10,
        verbose=False,
    )
# ------------------------
# Main pipeline
# ------------------------
def main():
    path=input("Enter the abs path of the directory, you what to organise:  ").strip()
    while not os.path.exists(path):
        print(f'Path {path} does not exist. Kindly enter a valid path.')
        path=input("Enter the abs path of the directory, you what to organise.").strip()

    print(f"Input path successfully set to {path}")
    print(f"""
    
{path}""")
    print(tree_builder(path))

    # Load models
    print("Loading model.....")
    llm = load_llm_text()
    print('Loading models complete......')
    print("""
    
    
    """)
    # Collect file paths
    print("Accessing files......")
    all_files = collect_file_path(path)
    # Prepare text content
    path_text = [(file_path, read_file(file_path)) for file_path in all_files]
    print("Accessing files complete.....")
    print("""
    
    
    """)
    yes_no=input("Do you want to organise your directory?(y/n)")
    if(yes_no=="y"or yes_no=="Y"):
        output_path=input(f"""Enter the abs output path for the arranged directory.(Default will be {os.path.join(os.path.dirname(path),'organized_dir')}):  """)
        if not output_path:
            output_path=os.path.join(os.path.dirname(path),'organized_dir')
        print(f"""Output path successfully set to {output_path}
    
    
        """)
        print("Processing files...")
        result=process_files_text(path_text, llm)
        print("Processing files complete....")
        print(f"""
    
    
        """)
        print(tree_built_preview(result,output_path))

        x=input(f"""
    
    Do you want to make changes(y/n):""")
        if(x=='y' or x=='Y'):
            organise(result,output_path)
    yes_no = input("Do you want to query the model using a file? (y/n): ")
    while(yes_no=='y' or yes_no=='Y'):
        path_f=input("""Enter the abs path of the document.
(Note:In case you have organised your directory, enter the new path)
Path: """)
        text=read_file(path_f)
        ans=question(path,text,llm)
        print(f"Answer: {ans}")
        yes_no=input("Do you want to ask another question?(y/n)")
        
    return None
# ------------------------
# Run
# ------------------------
if __name__ == "__main__":
    main()





