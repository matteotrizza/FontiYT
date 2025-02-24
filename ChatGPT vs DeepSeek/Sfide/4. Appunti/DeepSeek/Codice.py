import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkhtmlview import HTMLLabel
import markdown2

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E3440")

        # Pannello a sinistra per la lista delle note
        self.left_panel = tk.Frame(root, bg="#3B4252", width=200)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        # Lista delle note
        self.note_list = tk.Listbox(self.left_panel, bg="#4C566A", fg="#ECEFF4", selectbackground="#81A1C1")
        self.note_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.note_list.bind("<<ListboxSelect>>", self.on_note_select)

        # Pulsante per creare una nuova nota
        self.new_note_button = tk.Button(self.left_panel, text="Nuova Nota", bg="#81A1C1", fg="#2E3440", command=self.create_note)
        self.new_note_button.pack(side=tk.BOTTOM, fill=tk.X)

        # Pannello a destra per l'editor e la visualizzazione
        self.right_panel = tk.Frame(root, bg="#2E3440")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Editor di testo per il markdown
        self.text_editor = tk.Text(self.right_panel, bg="#3B4252", fg="#ECEFF4", insertbackground="#ECEFF4")
        self.text_editor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.text_editor.bind("<KeyRelease>", self.update_preview)

        # Visualizzazione del markdown formattato
        self.html_label = HTMLLabel(self.right_panel, background="#2E3440")
        self.html_label.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Carica le note esistenti
        self.load_notes()

    def load_notes(self):
        """Carica tutte le note .md nella cartella corrente."""
        self.note_list.delete(0, tk.END)
        for file in os.listdir("."):
            if file.endswith(".md"):
                self.note_list.insert(tk.END, file)

    def on_note_select(self, event):
        """Gestisce la selezione di una nota dalla lista."""
        selected_note = self.note_list.get(self.note_list.curselection())
        with open(selected_note, "r", encoding="utf-8") as file:
            content = file.read()
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(tk.END, content)
            self.update_preview()

    def update_preview(self, event=None):
        """Aggiorna la preview del markdown."""
        markdown_text = self.text_editor.get(1.0, tk.END)
        html = markdown2.markdown(markdown_text)
        self.html_label.set_html(html)

    def create_note(self):
        """Crea una nuova nota."""
        note_name = simpledialog.askstring("Nuova Nota", "Nome della nota:")
        if note_name:
            if not note_name.endswith(".md"):
                note_name += ".md"
            with open(note_name, "w", encoding="utf-8") as file:
                file.write("# Nuova Nota\n")
            self.load_notes()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
