#!/usr/bin/env python
# coding: utf-8
import re
def q_a(path,text,ques,llm):
    prompt=f"""You are a smart financial assistant.

    You will be given the raw text extracted from a financial document. This document could be an invoice, receipt, ITR, bank statement, or salary slip.
    
    You will also be given a user question related to the document — for example: "What is the total sales for this month?" or "How much tax was paid?"

    Your job is to:
    1. Understand the document content.
    2. Extract relevant information.
    3. Answer the user's question accurately and concisely.

    If the document does not contain enough information to answer the question, reply with: **"Insufficient data in the document to answer this question."**

    Text:{text}
    Question:{ques}
    Answer:
    """
    completion=llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
    )
    ans=completion['choices'][0]['message']['content'].strip()
    ans = re.sub(r'^Answer:\s*', '', ans, flags=re.IGNORECASE).strip()
    return ans

def question(path,text,llm):
    ques=input("your question?: ")
    return q_a(path,text,ques,llm)

