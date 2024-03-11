from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import messagebox

def create_invoice(customer_name, items, total_amount, invoice_number):
    # Create a PDF canvas
    c = canvas.Canvas(f"Invoice_{invoice_number}.pdf", pagesize=letter)

    # Set up the content
    y = 750
    c.drawString(100, y, f"Invoice Number: {invoice_number}")
    y -= 20
    c.drawString(100, y, f"Customer Name: {customer_name}")
    y -= 40
    c.drawString(100, y, "Items:")
    for item in items:
        y -= 20
        c.drawString(120, y, f"- {item['name']}: ${item['price']}")
    y -= 40
    c.drawString(100, y, f"Total Amount: ${total_amount}")

    # Save the PDF
    c.save()

def generate_invoice():
    customer_name = entry_customer_name.get()
    items_text = entry_items.get("1.0", tk.END).strip().split("\n")
    items = []
    for item_text in items_text:
        name, price = item_text.split(":")
        items.append({"name": name.strip(), "price": float(price.strip())})
    total_amount = sum(item['price'] for item in items)
    invoice_number = entry_invoice_number.get()
    create_invoice(customer_name, items, total_amount, invoice_number)
    messagebox.showinfo("Success", f"Invoice generated successfully: Invoice_{invoice_number}.pdf")

# Create GUI
root = tk.Tk()
root.title("Invoice Generator")

# Customer Name
label_customer_name = tk.Label(root, text="Customer Name:")
label_customer_name.grid(row=0, column=0, padx=5, pady=5)
entry_customer_name = tk.Entry(root)
entry_customer_name.grid(row=0, column=1, padx=5, pady=5)

# Items
label_items = tk.Label(root, text="Items (Name: Price):")
label_items.grid(row=1, column=0, padx=5, pady=5)
entry_items = tk.Text(root, height=5, width=30)
entry_items.grid(row=1, column=1, padx=5, pady=5)

# Invoice Number
label_invoice_number = tk.Label(root, text="Invoice Number:")
label_invoice_number.grid(row=2, column=0, padx=5, pady=5)
entry_invoice_number = tk.Entry(root)
entry_invoice_number.grid(row=2, column=1, padx=5, pady=5)

# Generate Invoice Button
generate_button = tk.Button(root, text="Generate Invoice", command=generate_invoice)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

