import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Funzione per aggiungere un articolo alla lista
def aggiungi_articolo():
    articolo = entry_articolo.get()
    quantita = entry_quantita.get()
    if articolo and quantita:
        lista_spesa.insert("", "end", values=(articolo, quantita))
        entry_articolo.delete(0, tk.END)
        entry_quantita.delete(0, tk.END)
    else:
        messagebox.showwarning("Attenzione", "Inserisci sia l'articolo che la quantità!")

# Funzione per rimuovere un articolo dalla lista
def rimuovi_articolo():
    selected_item = lista_spesa.selection()
    if selected_item:
        lista_spesa.delete(selected_item)
    else:
        messagebox.showwarning("Attenzione", "Seleziona un articolo da rimuovere!")

# Funzione per esportare la lista in CSV
def esporta_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        articoli = []
        for child in lista_spesa.get_children():
            articoli.append(lista_spesa.item(child)['values'])
        df = pd.DataFrame(articoli, columns=["Prodotto", "Quantità"])
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Successo", "Lista esportata in CSV con successo!")

# Funzione per esportare la lista in PDF
def esporta_pdf():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        articoli = []
        for child in lista_spesa.get_children():
            articoli.append(lista_spesa.item(child)['values'])
        df = pd.DataFrame(articoli, columns=["Prodotto", "Quantità"])

        pdf = SimpleDocTemplate(file_path, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []

        # Intestazione
        intestazione = Paragraph("Lista della Spesa", styles['Title'])
        elements.append(intestazione)

        # Tabella
        data = [df.columns.to_list()] + df.values.tolist()
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        pdf.build(elements)
        messagebox.showinfo("Successo", "Lista esportata in PDF con successo!")

# Creazione della finestra principale
root = tk.Tk()
root.title("Gestione Lista della Spesa")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Stile moderno
style = ttk.Style()
style.theme_use("clam")

# Frame per l'input
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, sticky="ew")

# Campo di input per l'articolo
label_articolo = ttk.Label(frame_input, text="Articolo:")
label_articolo.grid(row=0, column=0, padx=5, pady=5)
entry_articolo = ttk.Entry(frame_input, width=30)
entry_articolo.grid(row=0, column=1, padx=5, pady=5)

# Campo di input per la quantità
label_quantita = ttk.Label(frame_input, text="Quantità:")
label_quantita.grid(row=0, column=2, padx=5, pady=5)
entry_quantita = ttk.Entry(frame_input, width=15)
entry_quantita.grid(row=0, column=3, padx=5, pady=5)

# Pulsanti per aggiungere e rimuovere articoli
button_aggiungi = ttk.Button(frame_input, text="Aggiungi", command=aggiungi_articolo)
button_aggiungi.grid(row=0, column=4, padx=5, pady=5)
button_rimuovi = ttk.Button(frame_input, text="Rimuovi", command=rimuovi_articolo)
button_rimuovi.grid(row=0, column=5, padx=5, pady=5)

# Lista della spesa
frame_lista = ttk.Frame(root, padding="10")
frame_lista.grid(row=1, column=0, sticky="nsew")

columns = ("Prodotto", "Quantità")
lista_spesa = ttk.Treeview(frame_lista, columns=columns, show="headings")
lista_spesa.heading("Prodotto", text="Prodotto")
lista_spesa.heading("Quantità", text="Quantità")
lista_spesa.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_spesa.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
lista_spesa.configure(yscrollcommand=scrollbar.set)

# Pulsanti per esportare
frame_esporta = ttk.Frame(root, padding="10")
frame_esporta.grid(row=2, column=0, sticky="ew")

button_esporta_csv = ttk.Button(frame_esporta, text="Esporta CSV", command=esporta_csv)
button_esporta_csv.grid(row=0, column=0, padx=5, pady=5)
button_esporta_pdf = ttk.Button(frame_esporta, text="Esporta PDF", command=esporta_pdf)
button_esporta_pdf.grid(row=0, column=1, padx=5, pady=5)

# Configurazione del layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Avvio dell'applicazione
root.mainloop()
