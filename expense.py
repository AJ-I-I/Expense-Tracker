import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.expense_listbox = tk.Listbox(root)
        self.expense_listbox.pack(pady=10)

        self.show_expenses_button = tk.Button(root, text="Show Expenses", command=self.show_expenses)
        self.show_expenses_button.pack()

    def add_expense(self):
        expense = self.expense_entry.get()
        if expense:
            self.expenses.append(expense)
            self.expense_entry.delete(0, tk.END)
            messagebox.showinfo("Expense Added", "Expense has been added!")

    def show_expenses(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_listbox.insert(tk.END, expense)

def main():
    root = tk.Tk()
    expense_tracker = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
