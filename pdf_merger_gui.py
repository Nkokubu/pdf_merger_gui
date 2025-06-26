import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def merge_pdfs_in_folder(folder_path, output_path):
    merger = PyPDF2.PdfMerger()

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_files.sort()  # Alphabetical order

    if len(pdf_files) < 2:
        messagebox.showwarning("Not Enough PDFs", "Please select a folder with at least two PDF files.")
        return

    for pdf in pdf_files:
        full_path = os.path.join(folder_path, pdf)
        merger.append(full_path)

    merger.write(output_path)
    merger.close()

    messagebox.showinfo("Success", f"✅ PDFs merged successfully into:\n{output_path}")

def select_folder_and_merge():
    folder_path = filedialog.askdirectory(title="Select Folder Containing PDFs")
    if not folder_path:
        return

    output_path = filedialog.asksaveasfilename(
        title="Save Merged PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        initialfile="merged_output.pdf"
    )
    if not output_path:
        return

    merge_pdfs_in_folder(folder_path, output_path)

# GUI Setup
root = tk.Tk()
root.title("PDF Merger")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="Merge all PDFs in a folder", font=("Arial", 12))
label.pack(pady=20)

merge_button = tk.Button(root, text="Select Folder & Merge", command=select_folder_and_merge, font=("Arial", 10))
merge_button.pack()

root.mainloop()
