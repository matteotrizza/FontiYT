import math
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from sympy import sin, cos, tan, log, sqrt, pi, E, symbols
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr

# Funzione per valutare l'espressione matematica
def calcola():
    try:
        # Legge l'espressione dalla casella di testo
        expr = input_var.get()
        transformations = standard_transformations + (implicit_multiplication_application,)
        parsed_expr = parse_expr(expr, transformations=transformations)
        risultato = parsed_expr.evalf()
        input_var.set(risultato)
    except Exception as e:
        input_var.set("Errore")

# Funzione per aggiungere testo al display
def aggiungi_tasto(valore):
    input_var.set(input_var.get() + str(valore))

# Funzione per cancellare il display
def cancella():
    input_var.set("")

# Creazione della finestra principale
app = tb.Window(themename="darkly")
app.title("Calcolatrice Scientifica")
app.geometry("400x600")

# Variabile per l'input
input_var = tk.StringVar()

# Display
display = ttk.Entry(app, textvariable=input_var, font=("Arial", 20), justify='right')
display.pack(fill="x", pady=10, padx=10)

# Pulsanti principali
bottoni = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
]

frame_bottoni = ttk.Frame(app)
frame_bottoni.pack(pady=10)

for riga in bottoni:
    frame_riga = ttk.Frame(frame_bottoni)
    frame_riga.pack(fill="x")
    for btn in riga:
        if btn == "=":
            b = ttk.Button(frame_riga, text=btn, command=calcola, style="success.TButton")
        else:
            b = ttk.Button(frame_riga, text=btn, command=lambda btn=btn: aggiungi_tasto(btn))
        b.pack(side="left", expand=True, fill="x", padx=5, pady=5)

# Funzioni avanzate
funzioni = [
    ("sin", "cos", "tan", "sqrt"),
    ("log", "pi", "e", "C")
]

frame_funzioni = ttk.Frame(app)
frame_funzioni.pack(pady=10)

for riga in funzioni:
    frame_riga = ttk.Frame(frame_funzioni)
    frame_riga.pack(fill="x")
    for btn in riga:
        if btn == "C":
            b = ttk.Button(frame_riga, text=btn, command=cancella, style="danger.TButton")
        else:
            b = ttk.Button(frame_riga, text=btn, command=lambda btn=btn: aggiungi_tasto(btn + "("))
        b.pack(side="left", expand=True, fill="x", padx=5, pady=5)

# Avvio dell'app
app.mainloop()
