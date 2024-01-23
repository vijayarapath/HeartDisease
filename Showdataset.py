import csv
import tkinter as tk  # PEP 8 recommends against `import *`.

# Create and set the GUI for the passScreen of the Password Manager.
passScreen = tk.Tk()
passScreen.geometry("600x800")
passScreen.resizable(width=False, height=False)
passScreen.title("Load Dataset")

"""col_names = ("age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target")
for i, col_name in enumerate(col_names, start=1):
    tk.Label(passScreen, text=col_name).grid(row=3, column=i, padx=40)"""

with open("heart.csv", "r", newline="") as passfile:
    reader = csv.reader(passfile)
    data = list(reader)

entrieslist = []
for i, row in enumerate(data, start=4):
    entrieslist.append(row[0])
    for col in range(1, 8):
        tk.Label(passScreen, text=row[col]).grid(row=i, column=col)

passScreen.mainloop()
