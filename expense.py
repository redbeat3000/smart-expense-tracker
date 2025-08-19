import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from tabulate import tabulate
from fpdf import FPDF

# -----------------------------
# Database setup
# -----------------------------
conn = sqlite3.connect("expenses.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL, type TEXT)''')
conn.commit()

# -----------------------------
# Add expense or income
# -----------------------------
def add_record(record_type):
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Transport, Salary): ").strip()
    amount = float(input("Enter amount: ").strip())
    c.execute("INSERT INTO expenses (date, category, amount, type) VALUES (?, ?, ?, ?)",
              (date, category, amount, record_type))
    conn.commit()
    print(f"{record_type} recorded!\n")

# -----------------------------
# Generate monthly report
# -----------------------------
def generate_report():
    month = input("Enter month to report (YYYY-MM): ").strip()
    c.execute("SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? AND type='Expense' GROUP BY category", (f"{month}%",))
    data = c.fetchall()
    
    if not data:
        print("No expenses for this month.")
        return
    
    # Display table
    print("\n--- Monthly Expenses ---")
    print(tabulate(data, headers=["Category", "Total Amount"]))
    
    # Pie chart
    categories, amounts = zip(*data)
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title(f"Expenses Breakdown for {month}")
    chart_file = f"{month}_expenses.png"
    plt.savefig(chart_file)
    plt.close()
    
    # Export PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Expense Report for {month}", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Expenses by Category:", ln=True)
    pdf.set_font("Arial", '', 12)
    for cat, amt in data:
        pdf.cell(0, 10, f"{cat}: {amt}", ln=True)
    
    pdf.image(chart_file, x=30, y=80, w=150)
    pdf.output(f"{month}_expense_report.pdf")
    print(f"\nPDF report exported: {month}_expense_report.pdf")

# -----------------------------
# Main Program
# -----------------------------
def main():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Generate Monthly Report")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_record("Expense")
        elif choice == '2':
            add_record("Income")
        elif choice == '3':
            generate_report()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
