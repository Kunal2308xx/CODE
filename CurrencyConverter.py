from currency_converter import CurrencyConverter
import tkinter as tk
a=CurrencyConverter()
root=tk.Tk()
root.geometry("500x360")
def clicked():
    amount=int(ent.get())
    cur1=ent1.get()
    cur2=ent2.get()
    data=a.convert(amount,cur1, cur2)
    lb5=tk.Label(root, text="Coverted Currency:", font="Calibri 14 bold").place(x=50,y=320)
    ent4=tk.Label(root,text=data,font="Calibri 14 bold").place(x=215,y=320)

root.title("Currency Converter")
lb1=tk.Label(root, text="Currency Converter", font="Calibri 25 bold").place(x=100,y=30)
lb2=tk.Label(root, text="Enter Amount:", font="Calibri 14 bold").place(x=50,y=100)
ent=tk.Entry(root)
lb3=tk.Label(root, text="Enter Currency:", font="Calibri 14 bold").place(x=50,y=150)
ent1=tk.Entry(root)
lb4=tk.Label(root, text="Enter Req.Currency:", font="Calibri 14 bold").place(x=50,y=200)
ent2=tk.Entry(root)

btn=tk.Button(root,text="Click to Convert", command=clicked).place(x=200, y=270)

ent.place(x=215,y=107)
ent1.place(x=215,y=160)
ent2.place(x=215,y=207)

root.mainloop()