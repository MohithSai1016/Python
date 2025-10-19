import tkinter as tk
from tkinter import messagebox

def submit_details():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if name == "" or email == "" or age == "":
        messagebox.showwarning("Input Error", "Please fill all the fields!")
        return

    if len(name) > 35:
        messagebox.showwarning("Input Error", "Name cannot exceed 35 characters!")
        return

    if not email.endswith("@gmail.com"):
        messagebox.showwarning("Input Error", "Email must end with '@gmail.com'!")
        return

    if not age.isdigit():
        messagebox.showwarning("Input Error", "Age must be a number (integer only)!")
        return

  
    messagebox.showinfo("Confirmation", f"Thank you, {name}!\nYour details have been recorded successfully.")
    
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def limit_name_length(*args):
    value = name_var.get()
    if len(value) > 35:
        name_var.set(value[:35]) 

def validate_age_input(new_value):
    """Allow only digits for age."""
    if new_value == "" or new_value.isdigit():
        return True
    else:
        root.bell()
        return False

root = tk.Tk()
root.title("User Login Form")
root.geometry("800x700")

tk.Label(root, text="User Login Form", font=("Arial", 30, "bold")).pack(pady=20)

tk.Label(root, text="Name:", font=("Arial", 20)).pack()
name_var = tk.StringVar()
name_var.trace("w", limit_name_length)
name_entry = tk.Entry(root, width=40, font=("Arial", 20), textvariable=name_var)
name_entry.pack(pady=15)

tk.Label(root, text="Email:", font=("Arial", 20)).pack()
email_entry = tk.Entry(root, width=40, font=("Arial", 20))
email_entry.pack(pady=15)

tk.Label(root, text="Age:", font=("Arial", 20)).pack()
validate_age = root.register(validate_age_input)
age_entry = tk.Entry(root, width=40, font=("Arial", 20), validate="key", validatecommand=(validate_age, "%P"))
age_entry.pack(pady=15)

tk.Button(root, text="Submit", bg="black", fg="white", font=("Arial", 20, "bold"),
          height=2, width=12, command=submit_details).pack(pady=40)

root.mainloop()
