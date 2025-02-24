import os
import tkinter as tk
from tkinter import filedialog, ttk
from tkhtmlview import HTMLLabel
import markdown

# Installazione delle librerie necessarie: pip install tkhtmlview markdown

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Note Editor")
        self.root.geometry("800x600")

        # Stile moderno
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=("Arial", 12), rowheight=25)
        style.configure("TButton", font=("Arial", 12))

        self.create_widgets()
        self.load_notes()

    def create_widgets(self):
        # Frame sinistro per la lista di file
        self.left_frame = ttk.Frame(self.root, width=200)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.file_list = ttk.Treeview(self.left_frame, selectmode="browse")
        self.file_list.heading("#0", text="Notes", anchor=tk.W)
        self.file_list.pack(fill=tk.BOTH, expand=True)
        self.file_list.bind("<Double-1>", self.open_note)

        self.new_note_button = ttk.Button(self.left_frame, text="New Note", command=self.create_note)
        self.new_note_button.pack(pady=5)

        # Frame destro per l'editor e la preview
        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.editor = tk.Text(self.right_frame, font=("Arial", 12), wrap=tk.WORD)
        self.editor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.preview_label = HTMLLabel(self.right_frame, background="white")
        self.preview_label.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.save_button = ttk.Button(self.right_frame, text="Save", command=self.save_note)
        self.save_button.pack(pady=5)

    def load_notes(self):
        self.file_list.delete(*self.file_list.get_children())
        for file in os.listdir():
            if file.endswith(".md"):
                self.file_list.insert("", tk.END, text=file)

    def open_note(self, event):
        selected_item = self.file_list.selection()
        if selected_item:
            file_name = self.file_list.item(selected_item, "text")
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
                self.editor.delete(1.0, tk.END)
                self.editor.insert(tk.END, content)
                self.preview_markdown(content)
            self.current_file = file_name

    def save_note(self):
        if hasattr(self, "current_file"):
            content = self.editor.get(1.0, tk.END).strip()
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(content)
            self.preview_markdown(content)
            self.load_notes()

    def create_note(self):
        new_file_name = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
        if new_file_name:
            with open(new_file_name, "w", encoding="utf-8") as f:
                f.write("")
            self.load_notes()

    def preview_markdown(self, content):
        html_content = markdown.markdown(content)
        self.preview_label.set_html(html_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownEditor(root)
    root.mainloop()
