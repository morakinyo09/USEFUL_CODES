import tkinter as tk
from tkinter import messagebox
import sqlite3

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Database setup
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.setup_database()

        # Expense name input
        self.name_label = tk.Label(root, text="Expense Name:")
        self.name_label.pack()
        self.name_input = tk.Entry(root, width=50)
        self.name_input.pack(pady=5)

        # Expense amount input
        self.amount_label = tk.Label(root, text="Expense Amount:")
        self.amount_label.pack()
        self.amount_input = tk.Entry(root, width=50)
        self.amount_input.pack(pady=5)

        # Expense date input
        self.date_label = tk.Label(root, text="Expense Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_input = tk.Entry(root, width=50)
        self.date_input.pack(pady=5)

        # Add expense button
        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=10)

        # Expense listbox
        self.expense_listbox = tk.Listbox(root, width=50, height=15)
        self.expense_listbox.pack(pady=10)

        # Remove expense button
        self.remove_expense_button = tk.Button(root, text="Remove Expense", command=self.remove_expense)
        self.remove_expense_button.pack(pady=5)

        # Total expense label
        self.total_label = tk.Label(root, text="Total Expense: $0.00")
        self.total_label.pack(pady=5)

        self.load_expenses()

    def setup_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_expense(self):
        name = self.name_input.get()
        amount = self.amount_input.get()
        date = self.date_input.get()

        if not name or not amount or not date:
            messagebox.showwarning("Warning", "All fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Warning", "Amount must be a number.")
            return

        self.cursor.execute("INSERT INTO expenses (name, amount, date) VALUES (?, ?, ?)", (name, amount, date))
        self.conn.commit()

        self.expense_listbox.insert(tk.END, f"{date} - {name}: ${amount:.2f}")

        self.name_input.delete(0, tk.END)
        self.amount_input.delete(0, tk.END)
        self.date_input.delete(0, tk.END)

        self.update_total()

    def remove_expense(self):
        selected_expense_index = self.expense_listbox.curselection()
        if selected_expense_index:
            expense_text = self.expense_listbox.get(selected_expense_index)
            date, rest = expense_text.split(" - ", 1)
            name, amount_text = rest.rsplit(": $", 1)
            amount = float(amount_text)

            self.cursor.execute("DELETE FROM expenses WHERE name = ? AND amount = ? AND date = ?", (name, amount, date))
            self.conn.commit()

            self.expense_listbox.delete(selected_expense_index)
            self.update_total()
        else:
            messagebox.showwarning("Warning", "You must select an expense to remove.")

    def load_expenses(self):
        self.cursor.execute("SELECT date, name, amount FROM expenses")
        rows = self.cursor.fetchall()
        for row in rows:
            date, name, amount = row
            self.expense_listbox.insert(tk.END, f"{date} - {name}: ${amount:.2f}")

        self.update_total()

    def update_total(self):
        self.cursor.execute("SELECT SUM(amount) FROM expenses")
        total_amount = self.cursor.fetchone()[0]
        if total_amount is None:
            total_amount = 0
        self.total_label.config(text=f"Total Expense: ${total_amount:.2f}")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
