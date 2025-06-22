import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfMerger, PdfReader, PdfWriter


class PDFToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger and Splitter")
        self.root.geometry("600x500")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', padding=6, relief='flat', background='#ccc')
        self.style.configure('TLabel', background='#f0f0f0', padding=5)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each tab
        self.merge_frame = ttk.Frame(self.notebook)
        self.split_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.merge_frame, text='Merge PDFs')
        self.notebook.add(self.split_frame, text='Split PDF')
        
        # Initialize UI for both tabs
        self.setup_merge_tab()
        self.setup_split_tab()
        
    def setup_merge_tab(self):
        # Merge PDFs UI
        merge_label = ttk.Label(self.merge_frame, text="Select PDF files to merge:", font=('Arial', 12))
        merge_label.pack(pady=10)
        
        # Listbox to display selected files
        self.merge_listbox = tk.Listbox(self.merge_frame, selectmode=tk.EXTENDED, height=10, width=70)
        self.merge_listbox.pack(pady=5, padx=10, fill='both', expand=True)
        
        # Scrollbar for listbox
        scrollbar = ttk.Scrollbar(self.merge_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.merge_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.merge_listbox.yview)
        
        # Buttons frame
        merge_btn_frame = ttk.Frame(self.merge_frame)
        merge_btn_frame.pack(pady=10)
        
        # Add files button
        add_btn = ttk.Button(merge_btn_frame, text="Add PDFs", command=self.add_pdfs)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Remove selected button
        remove_btn = ttk.Button(merge_btn_frame, text="Remove Selected", command=self.remove_selected)
        remove_btn.pack(side=tk.LEFT, padx=5)
        
        # Move up button
        up_btn = ttk.Button(merge_btn_frame, text="Move Up", command=lambda: self.move_item(-1))
        up_btn.pack(side=tk.LEFT, padx=5)
        
        # Move down button
        down_btn = ttk.Button(merge_btn_frame, text="Move Down", command=lambda: self.move_item(1))
        down_btn.pack(side=tk.LEFT, padx=5)
        
        # Output filename
        output_frame = ttk.Frame(self.merge_frame)
        output_frame.pack(pady=10, fill='x', padx=10)
        
        ttk.Label(output_frame, text="Output Filename:").pack(side=tk.LEFT)
        self.output_name = tk.StringVar(value="merged.pdf")
        output_entry = ttk.Entry(output_frame, textvariable=self.output_name, width=40)
        output_entry.pack(side=tk.LEFT, padx=5)
        
        # Merge button
        merge_btn = ttk.Button(self.merge_frame, text="Merge PDFs", command=self.merge_pdfs)
        merge_btn.pack(pady=10)
    
    def setup_split_tab(self):
        # Split PDF UI
        split_label = ttk.Label(self.split_frame, text="Select PDF file to split:", font=('Arial', 12))
        split_label.pack(pady=10)
        
        # Selected file label
        self.split_file_label = ttk.Label(self.split_frame, text="No file selected", wraplength=500)
        self.split_file_label.pack(pady=5)
        
        # Select file button
        select_btn = ttk.Button(self.split_frame, text="Select PDF", command=self.select_split_file)
        select_btn.pack(pady=5)
        
        # Output folder
        output_folder_frame = ttk.Frame(self.split_frame)
        output_folder_frame.pack(pady=10, fill='x', padx=10)
        
        ttk.Label(output_folder_frame, text="Output Folder:").pack(side=tk.LEFT)
        self.output_folder = tk.StringVar()
        output_entry = ttk.Entry(output_folder_frame, textvariable=self.output_folder, width=40)
        output_entry.pack(side=tk.LEFT, padx=5)
        browse_btn = ttk.Button(output_folder_frame, text="Browse", command=self.select_output_folder)
        browse_btn.pack(side=tk.LEFT)
        
        # Prefix for split files
        prefix_frame = ttk.Frame(self.split_frame)
        prefix_frame.pack(pady=5, fill='x', padx=10)
        
        ttk.Label(prefix_frame, text="File Prefix:").pack(side=tk.LEFT)
        self.file_prefix = tk.StringVar(value="page_")
        prefix_entry = ttk.Entry(prefix_frame, textvariable=self.file_prefix, width=20)
        prefix_entry.pack(side=tk.LEFT, padx=5)
        
        # Split button
        split_btn = ttk.Button(self.split_frame, text="Split PDF", command=self.split_pdf)
        split_btn.pack(pady=10)
    
    def add_pdfs(self):
        filetypes = [("PDF files", "*.pdf"), ("All files", "*.*")]
        files = filedialog.askopenfilenames(title="Select PDF files", filetypes=filetypes)
        
        if files:
            for file in files:
                self.merge_listbox.insert(tk.END, file)
    
    def remove_selected(self):
        selected = self.merge_listbox.curselection()
        for index in selected[::-1]:  # Delete from back to front to avoid index issues
            self.merge_listbox.delete(index)
    
    def move_item(self, direction):
        selected = self.merge_listbox.curselection()
        if not selected:
            return
        
        index = selected[0]
        if (direction == -1 and index == 0) or (direction == 1 and index == self.merge_listbox.size() - 1):
            return
        
        item = self.merge_listbox.get(index)
        self.merge_listbox.delete(index)
        self.merge_listbox.insert(index + direction, item)
        self.merge_listbox.selection_set(index + direction)
    
    def merge_pdfs(self):
        if self.merge_listbox.size() == 0:
            messagebox.showerror("Error", "No PDF files selected to merge")
            return
        
        output_filename = self.output_name.get()
        if not output_filename:
            messagebox.showerror("Error", "Please specify an output filename")
            return
        
        if not output_filename.lower().endswith('.pdf'):
            output_filename += '.pdf'
        
        merger = PdfMerger()
        
        try:
            for i in range(self.merge_listbox.size()):
                pdf_path = self.merge_listbox.get(i)
                merger.append(pdf_path)
            
            # Ask for save location
            save_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialfile=output_filename,
                title="Save merged PDF as"
            )
            
            if save_path:
                with open(save_path, 'wb') as f:
                    merger.write(f)
                messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved as: {save_path}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")
        finally:
            merger.close()
    
    def select_split_file(self):
        filetypes = [("PDF files", "*.pdf"), ("All files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select PDF file to split", filetypes=filetypes)
        
        if file_path:
            self.split_file_path = file_path
            self.split_file_label.config(text=file_path)
    
    def select_output_folder(self):
        folder_path = filedialog.askdirectory(title="Select output folder")
        if folder_path:
            self.output_folder.set(folder_path)
    
    def split_pdf(self):
        if not hasattr(self, 'split_file_path') or not self.split_file_path:
            messagebox.showerror("Error", "No PDF file selected to split")
            return
        
        output_folder = self.output_folder.get()
        if not output_folder:
            messagebox.showerror("Error", "Please select an output folder")
            return
        
        prefix = self.file_prefix.get()
        if not prefix:
            prefix = "page_"
        
        try:
            with open(self.split_file_path, 'rb') as f:
                reader = PdfReader(f)
                total_pages = len(reader.pages)
                
                if total_pages == 0:
                    messagebox.showerror("Error", "The selected PDF has no pages")
                    return
                
                for i in range(total_pages):
                    writer = PdfWriter()
                    writer.add_page(reader.pages[i])
                    
                    output_filename = f"{prefix}{i+1}.pdf"
                    output_path = os.path.join(output_folder, output_filename)
                    
                    with open(output_path, 'wb') as out_f:
                        writer.write(out_f)
                
                messagebox.showinfo("Success", f"PDF split successfully!\n{total_pages} pages created in:\n{output_folder}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to split PDF:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToolApp(root)
    root.mainloop()
