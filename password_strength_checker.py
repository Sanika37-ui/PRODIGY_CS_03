import tkinter as tk
import re

def check_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    number = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(upper), bool(lower), bool(number), bool(special)])

    if score == 5:
        return "Strong", "green"
    elif score >= 3:
        return "Moderate", "orange"
    else:
        return "Weak", "red"

def on_key_release(event=None):
    password = entry.get()
    strength, color = check_strength(password)
    label_result.config(text=strength, fg=color)

    requirements = [
        (len(password) >= 8, "✔ At least 8 characters"),
        (re.search(r"[A-Z]", password), "✔ Contains uppercase letter"),
        (re.search(r"[a-z]", password), "✔ Contains lowercase letter"),
        (re.search(r"[0-9]", password), "✔ Contains number"),
        (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "✔ Contains special character")
    ]

    for i, (valid, text) in enumerate(requirements):
        checklist[i].config(text=text, fg="green" if valid else "red")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.configure(bg="#f9f9f9")

tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#f9f9f9").pack(pady=(20, 5))
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack()
entry.bind("<KeyRelease>", on_key_release)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f9f9f9")
label_result.pack(pady=10)

checklist = []
for _ in range(5):
    lbl = tk.Label(root, text="", font=("Arial", 10), anchor="w", bg="#f9f9f9")
    lbl.pack(fill='x', padx=30, anchor="w")
    checklist.append(lbl)

root.mainloop()
