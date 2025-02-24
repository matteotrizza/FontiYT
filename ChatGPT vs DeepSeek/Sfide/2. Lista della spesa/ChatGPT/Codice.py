import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
from fpdf import FPDF

def install_dependencies():
    try:
        import pip
        pip.main(['install', 'fpdf'])
    except:
        print("Please install the required libraries using: pip install fpdf")

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List Manager")
        self.root.geometry("600x400")
        
        self.shopping_list = []

        # Main frame
        frame = ttk.Frame(root, padding=10)
        frame.grid(row=0, column=0, sticky="nsew")
        
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Input fields
        self.product_label = ttk.Label(frame, text="Product:")
        self.product_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.product_entry = ttk.Entry(frame)
        self.product_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        
        self.quantity_label = ttk.Label(frame, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.quantity_entry = ttk.Entry(frame)
        self.quantity_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        frame.columnconfigure(1, weight=1)

        # Buttons for adding/removing
        self.add_button = ttk.Button(frame, text="Add", command=self.add_item)
        self.add_button.grid(row=2, column=0, pady=5, padx=5)
        
        self.remove_button = ttk.Button(frame, text="Remove", command=self.remove_item)
        self.remove_button.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        # Shopping list display
        self.tree = ttk.Treeview(frame, columns=("Product", "Quantity"), show="headings")
        self.tree.heading("Product", text="Product")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        frame.rowconfigure(3, weight=1)

        # Export buttons
        self.export_csv_button = ttk.Button(frame, text="Export to CSV", command=self.export_csv)
        self.export_csv_button.grid(row=4, column=0, pady=10, padx=5, sticky="ew")
        
        self.export_pdf_button = ttk.Button(frame, text="Export to PDF", command=self.export_pdf)
        self.export_pdf_button.grid(row=4, column=1, pady=10, padx=5, sticky="ew")

    def add_item(self):
        product = self.product_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        if product and quantity:
            self.shopping_list.append((product, quantity))
            self.tree.insert("", "end", values=(product, quantity))
            self.product_entry.delete(0, "end")
            self.quantity_entry.delete(0, "end")
        else:
            messagebox.showerror("Input Error", "Please fill both fields")

    def remove_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                values = self.tree.item(item, "values")
                self.shopping_list.remove(values)
                self.tree.delete(item)
        else:
            messagebox.showerror("Selection Error", "No item selected")

    def export_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filepath:
            with open(filepath, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Product", "Quantity"])
                writer.writerows(self.shopping_list)
            messagebox.showinfo("Export Successful", f"List exported to {filepath}")

    def export_pdf(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filepath:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Shopping List", ln=True, align="C")
            pdf.ln(10)

            for product, quantity in self.shopping_list:
                pdf.cell(200, 10, txt=f"{product}: {quantity}", ln=True)

            pdf.output(filepath)
            messagebox.showinfo("Export Successful", f"PDF exported to {filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
