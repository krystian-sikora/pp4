from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(brutto.get())
        taxvalue = float(tax.get())
        netto.set(round(value - value * taxvalue / 100, 2))
    except ValueError:
        pass

root = Tk()
root.title("Brutto to Netto Calculator")

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

brutto = StringVar()
brutto_entry = ttk.Entry(mainframe, textvariable = brutto)
brutto_entry.grid(column = 2, row = 1, sticky = (W, E))

tax = StringVar()
tax_entry = ttk.Entry(mainframe, textvariable = tax)
tax_entry.grid(column = 2, row = 2, sticky = (W, E))

netto = StringVar()
ttk.Label(mainframe, textvariable = netto).grid(column = 2, row = 3, sticky = (W, E))

ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 3, row = 4, sticky = W)

ttk.Label(mainframe, text = "brutto").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "after").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "% tax").grid(column = 3, row = 2, sticky = W)
ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 3, sticky = E)
ttk.Label(mainframe, text = "netto").grid(column = 3, row = 3, sticky = W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

brutto_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()

        