from tkinter import *
from tkinter import messagebox

f = ('Times', 14)


def compute_area():
    w = tWidth.get()
    if w == 'clerk':
        clerk_pay()
    elif w == 'supervisor':
        super_pay()
    elif w == 'manager':
        manager_pay()

    messagebox.showinfo('confirmation', 'Area = ' + str(area))
def clerk_pay():
    clerk = 250
    h = float(thour.get())
    pay = h * clerk
    tax = pay * .12
    pay = pay + tax
    messagebox.showinfo('confirmation', 'Final pay (tax included) = ' + str(pay))
def super_pay():
    super = 450
    h = float(thour.get())
    pay = h * super
    tax = pay * .12
    pay = pay + tax
    messagebox.showinfo('confirmation', 'Final pay (tax included) = ' + str(pay))
def manager_pay():
    manager = 650
    h = float(thour.get())
    pay = h * manager
    tax = pay * .12
    pay = pay + tax
    messagebox.showinfo('confirmation', 'Final pay (tax included) = ' + str(pay))
ws = Tk()
ws.title('Pay Calculator')
ws.geometry('400x300')
ws.config(bg='#0B5A81')

frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    frame,
    text="Hour",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    frame,
    text="Position [clerk/supervisor/manager]",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

thour = Entry(
    frame,
    font=f
)
tWidth = Entry(
    frame,
    font=f
)
bCompute = Button(
    frame,
    width=15,
    text='Compute',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=compute_area
)

thour.grid(row=0, column=1, pady=10, padx=20)
tWidth.grid(row=1, column=1, pady=10, padx=20)
bCompute.grid(row=2, column=1, pady=10, padx=20)
frame.place(x=50, y=50)

ws.mainloop()
