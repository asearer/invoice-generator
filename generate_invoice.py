import PyPDF2

def create_invoice(customer_name, items, total_amount, invoice_number):
    # Create a PDF object
    pdf = PyPDF2.PdfFileWriter()

    # Add a new page
    page = pdf.add_page()

    # Set up a PDF content stream
    content = f"Invoice Number: {invoice_number}\n\nCustomer Name: {customer_name}\n\nItems:\n"
    for item in items:
        content += f"- {item['name']}: ${item['price']}\n"
    content += f"\nTotal Amount: ${total_amount}"

    # Add content to the page
    page.mergePage(content)

    # Save the PDF to a file
    with open(f"Invoice_{invoice_number}.pdf", "wb") as file:
        pdf.write(file)

# Example usage
customer_name = "John Doe"
items = [
    {"name": "Service A", "price": 100},
    {"name": "Service B", "price": 150},
]
total_amount = sum(item['price'] for item in items)
invoice_number = "INV001"

create_invoice(customer_name, items, total_amount, invoice_number)
