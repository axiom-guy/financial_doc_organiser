#!/usr/bin/env python
# coding: utf-8

import re
import os
import time
from alive_progress import alive_bar

def generate_name_text_local(path,text,bar,llm):
    prompt = f"""You are a smart financial assistant.
    Classify the following document into one of the following categories:
    ["invoice", "receipt", "bank statement", "ITR", "salary slip", "unknown"]
    Text: {text}
    Return only the category name.
    Category:"""
    completion_summarize=llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
    )
    foldername=completion_summarize['choices'][0]['message']['content'].strip()
    print(foldername)
    bar()

    file_prompt = f"""
    You are a smart financial assistant.

    Generate a concise and meaningful filename for a document classified as: "{foldername}".

    - Read the document content.
    - Use at most 10 words.
    - Join the words with underscores (_).
    - Do NOT include the file extension.
    - Do NOT add any additional explanation.

    Text:{text}
    Just output the filename, no need for other information.
    Filename:
    """
    completion_filename=llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"{file_prompt}"
            }
        ],
    )
    filename=completion_filename['choices'][0]['message']['content'].strip()
    filename = re.sub(r'^Filename:\s*', '', filename, flags=re.IGNORECASE).strip()
    print(filename)
    bar()
    if not filename:
        filename='Untitled'
    if not foldername:
        foldername="Untitled"
    return (filename,foldername)

def process_file_text_local(path_text,llm):
    path,text=path_text
    start=time.time()
    with alive_bar(2,title=f"Processing {os.path.basename(path)}") as bar:
        filename,foldername=generate_name_text_local(path,text,bar,llm)
    end=time.time()

    print(f"File:{os.path.basename(path)}. Processing done in {end-start:.2f}")

    return {"path":path,"file_name":filename,"folder_name":foldername}


def process_files_text(path_text_files,llm):
    result=[]
    for path_text in path_text_files:
        result.append(process_file_text_local(path_text,llm))
    return result

