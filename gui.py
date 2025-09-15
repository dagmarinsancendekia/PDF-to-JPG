import tkinter as tk
from tkinter import filedialog, messagebox
from main import pdf_to_jpg, jpg_to_pdf

def convert_pdf_to_jpg():
    pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        output_dir = filedialog.askdirectory(title="Select output directory for JPG files")
        if output_dir:
            try:
                pdf_to_jpg(pdf_path, output_dir)
                messagebox.showinfo("Success", f"PDF converted to JPG in {output_dir}")
            except Exception as e:
                messagebox.showerror("Error", f"Conversion failed: {str(e)}")

def convert_jpg_to_pdf():
    jpg_paths = filedialog.askopenfilenames(title="Select JPG files", filetypes=[("JPG files", "*.jpg")])
    if jpg_paths:
        output_pdf = filedialog.asksaveasfilename(title="Save PDF as", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_pdf:
            try:
                jpg_to_pdf(list(jpg_paths), output_pdf)
                messagebox.showinfo("Success", f"JPGs converted to PDF: {output_pdf}")
            except Exception as e:
                messagebox.showerror("Error", f"Conversion failed: {str(e)}")

root = tk.Tk()
root.title("PDF to JPG and JPG to PDF Converter")
root.geometry("400x200")

btn_pdf_to_jpg = tk.Button(root, text="Convert PDF to JPG", command=convert_pdf_to_jpg, width=20, height=2)
btn_pdf_to_jpg.pack(pady=20)

btn_jpg_to_pdf = tk.Button(root, text="Convert JPG to PDF", command=convert_jpg_to_pdf, width=20, height=2)
btn_jpg_to_pdf.pack(pady=20)

root.mainloop()
