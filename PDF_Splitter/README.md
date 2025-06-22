# 📄 PDF Merger and Splitter Tool

A simple and efficient Python GUI application for managing PDF files.
With this tool, you can:

* ✅ Merge multiple PDF files into one
* ✂️ Split a single PDF into separate pages

---

## 🚀 Features

### 🔗 Merge PDFs

* Add multiple PDF files
* Reorder files before merging
* Remove selected PDFs from the list
* Set a custom output filename
* Choose where to save the merged file

### 📂 Split PDFs

* Select a PDF file to split
* Set an output directory for the split files
* Add a custom filename prefix (default: `page_`)
* Automatically split each page into a separate file

---

## 🛠️ Built With

* [**PyPDF2**](https://pypi.org/project/PyPDF2/) — for handling PDF operations
* [**Tkinter**](https://docs.python.org/3/library/tkinter.html) — for the graphical user interface

---

## 📥 Installation

### ✅ Prerequisites

* Python 3.x installed on your system

### 💡 Steps to Install

1. Clone or download this repository.
2. Install required packages:

   ```bash
   pip install PyPDF2
   ```
3. Run the application:

   ```bash
   python pdf_tool.py
   ```

---

## 💻 Usage

### 1. Launch the Application

* Run the following command in your terminal:

  ```bash
  python pdf_tool.py
  ```
* A GUI window will appear with two tabs: **"Merge PDFs"** and **"Split PDF"**

---

### 2. Merge PDFs

* Navigate to the **"Merge PDFs"** tab
* Click **"Add PDFs"** to select files
* Use **"Move Up"**, **"Move Down"**, or **"Remove"** to organize the list
* Set a custom output filename (default: `merged.pdf`)
* Click **"Merge PDFs"** and select the output location

---

### 3. Split a PDF

* Navigate to the **"Split PDF"** tab
* Click **"Select PDF"** to choose a file
* Click **"Browse"** to set the output folder
* Set a filename prefix for output pages (default: `page_`)
* Click **"Split PDF"** to generate individual page files

---

## 🧰 Troubleshooting

### Common Issues

1. **File Not Found Errors**

   * Ensure all selected PDF paths are valid
   * Don’t move or rename files after adding them

2. **Permission Errors**

   * Make sure you have write permissions in the selected output directory

3. **Corrupted PDF Files**

   * Verify the file opens in a standard PDF viewer

### Error Messages

The application provides clear error messages for most issues.
If you run into persistent problems, please include the following when reporting:

* Exact error message
* Steps to reproduce the issue
* Your OS and Python version
