import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []

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
        self.total_label = tk.Label(root, text="Total Expense: #0.00")
        self.total_label.pack(pady=5)

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

        expense = f"{date} - {name}: #{amount:.2f}"
        self.expenses.append((date, name, amount))
        self.expense_listbox.insert(tk.END, expense)

        self.name_input.delete(0, tk.END)
        self.amount_input.delete(0, tk.END)
        self.date_input.delete(0, tk.END)

        self.update_total()

    def remove_expense(self):
        selected_expense_index = self.expense_listbox.curselection()
        if selected_expense_index:
            self.expenses.pop(selected_expense_index[0])
            self.expense_listbox.delete(selected_expense_index)
            self.update_total()
        else:
            messagebox.showwarning("Warning", "You must select an expense to remove.")

    def update_total(self):
        total_amount = sum(expense[2] for expense in self.expenses)
        self.total_label.config(text=f"Total Expense: #{total_amount:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
