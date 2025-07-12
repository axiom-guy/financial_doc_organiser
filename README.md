# 📁 Financial Document Organizer

A smart AI-powered tool that helps you **automatically organize and query financial documents** (e.g. invoices, ITRs, bank statements) using LLMs (Large Language Models). It reads, classifies, and sorts documents into structured folders, and even allows you to ask questions about the contents of the files.

---

## 🚀 Features

- ✅ Organize financial documents into folders based on type and content.
- 🧠 Uses [LLaMA 3-8B Instruct GGUF](https://huggingface.co/MaziyarPanahi/Meta-Llama-3-8B-Instruct-GGUF) model locally for offline inference.
- 🧾 Supports various document types: invoices, bank statements, ITRs, salary slips, and more.
- ❓ Ask questions about any document (e.g. “What is the total sale for June?”).
- 📦 Creates a clean, previewable folder structure before actual organizing.
- 🔐 Works locally — your data never leaves your system.

---

## 🧱 Project Structure

```bash
project/
├── main.py                  # Main entrypoint for organizing and querying
├── text_processing.py       # Classification and metadata generation logic
├── tree_builder.py          # Builds a preview of directory tree
├── read_data.py             # File path collection and reading 
├── text_questioning.py      # Handles answering user questions on documents
├── common_functions.py      # Shared utility functions
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/axiom-guy/financial_doc_organiser.git
cd financial_doc_organiser
```
### 2. Creating and activating virtual environment
```bash
#create and activate a virtual environment
python -m venv financial_org
source financial_org/bin/activate
```
Make sure to upgrade your pip to latest version.
### 3. Installing dependencies
```bash
pip install -r requirements.txt
```
If facing issue while using llama-cpp-python, kindly check its [documentation](https://github.com/abetlen/llama-cpp-python.git).

## 🧪 How to Use

### 1.🔧 Step 1: Run the Script
```bash
python main.py
```
### 📂 Step 2: Provide Input Directory
Enter the absolute path of the directory containing your financial files.

### 🗂️ Step 3: Organize Files
You'll be prompted:<br>
-To choose whether to organize<br>
-To provide an output path (optional)<br>
-Preview the proposed structure<br>
-Confirm and organize<br>

### 💬 Step 4: Ask Questions
Ask natural language questions about any document, such as:
```text
“What is the income shown in this ITR?”
```
The assistant will read and answer from the file using the LLM.

## 📌 Contributions
Contributions are welcome! Feel free to fork, raise issues, or submit pull requests.
