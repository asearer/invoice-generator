from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

# Example usage
customer_name = "John Doe"
items = [
    {"name": "Service A", "price": 100},
    {"name": "Service B", "price": 150},
]
total_amount = sum(item['price'] for item in items)
invoice_number = "INV001"

create_invoice(customer_name, items, total_amount, invoice_number)
