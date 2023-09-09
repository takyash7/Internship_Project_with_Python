import tkinter as tk
from tkinter import messagebox
from tkinter import *

master = tk.Tk()

master.title("bills")

master.geometry("1000x500")

e1 = tk.Entry(master,font=10,justify="center")
e1.focus_set()
e2 = tk.Entry(master,font=10,justify="center")
e3 = tk.Entry(master,font=10,justify="center")
e4 = tk.Entry(master,font=10,justify="center")
e5 = tk.Entry(master,font=10,justify="center")
e6 = tk.Entry(master,font=10,justify="center")
e7 = tk.Entry(master,font=10,justify="center")
e8 = tk.Entry(master,font=10,justify="center")
e9 = tk.Entry(master,font=10,justify="center")
e10 = tk.Entry(master,font=10,justify="center")
e11 = tk.Entry(master,font=10,justify="center")
e12 = tk.Entry(master,font=10,justify="center")
e13 = tk.Entry(master,font=10,justify="center")
e14 = tk.Entry(master,font=10,justify="center")
e15 = tk.Entry(master,font=10,justify="center")
e16 = tk.Entry(master,font=10,justify="center")
e17 = tk.Entry(master,font=10,justify="center")
e18 = tk.Entry(master,font=10,justify="center")
e19 = tk.Entry(master,font=10,justify="center")

def display():
    
    entries = [e1, e2, e3, e4, e5, e6, e7, e8, e9,e10,e11,e12,e13,e14,e15,e15,e17,e18,e19]

    for entry in entries:
        if entry.get() == "":
            messagebox.showerror("Error", "All fields are mandatory")
            return

    qty1=0
    qty2=0
    qty3=0
    qty4=0
    qty5=0
    
    price1=0
    price2=0
    price3=0
    price4=0
    price5=0
    
    qty1 = int(e10.get())
    qty2 = int(e11.get())
    qty3 = int(e12.get())
    qty4 = int(e13.get())
    qty5 = int(e14.get())
    price1 = int(e15.get())
    price2 = int(e16.get())
    price3 = int(e17.get())
    price4 = int(e18.get())
    price5 = int(e19.get())
    
    t1 = qty1*price1
    t2 = qty2*price5
    t3 = qty3*price3
    t4 = qty4*price4
    t5 = qty5*price5
    
    total=t1+t2+t3+t4+t5
    
    gst=total*0.18
    total2=gst+total
    dis=total2*0.1
    gtotal=total2-dis
    
    tk.Label(master,text=t1,font=20).grid(row=8, column=5)
    tk.Label(master,text=t2,font=20).grid(row=9, column=5)
    tk.Label(master,text=t3,font=20).grid(row=10, column=5)
    tk.Label(master,text=t4,font=20).grid(row=11, column=5)
    tk.Label(master,text=t5,font=20).grid(row=12, column=5)
    
    tk.Label(master,fg="green",text=total,font=20).grid(row=14, column=5)
    tk.Label(master,fg="red",text="18 %",font=20).grid(row=15, column=5)
    tk.Label(master,fg="red",text="10 %",font=20).grid(row=16, column=5)
    tk.Label(master,fg="green",text=gtotal,font=20).grid(row=18, column=5)

tk.Label(master,fg="red", text="TAK'S   FABRICS",font=20).place(x=700,y=10)

tk.Label(master, fg="blue",text="Date",font=20).grid(row=3, column=1)
tk.Label(master,fg="blue", text="Gst. No",font=20).grid(row=4, column=1)
tk.Label(master,fg="blue", text="Customer Name",font=20).grid(row=3, column=4)
tk.Label(master,fg="blue", text="Mobile. No",font=20).grid(row=4, column=4)

tk.Label(master,fg="blue", text="Product Name",font=20).grid(row=7, column=2)
tk.Label(master,fg="blue", text="Qyantity",font=20).grid(row=7, column=3)
tk.Label(master,fg="blue", text="Price",font=20).grid(row=7, column=4)
tk.Label(master,fg="blue", text="Total",font=20).grid(row=7, column=5)

tk.Label(master, fg="blue",text="Sr No",font=20).grid(row=7, column=1)
tk.Label(master, text="1",font=20).grid(row=8, column=1)
tk.Label(master, text="2",font=20).grid(row=9, column=1)
tk.Label(master, text="3",font=20).grid(row=10, column=1)
tk.Label(master, text="4",font=20).grid(row=11, column=1)
tk.Label(master, text="5",font=20).grid(row=12, column=1)

tk.Label(master,fg="blue", text="Total Amount (RS)",font=20).grid(row=14, column=4)
tk.Label(master, fg="blue",text=" GST  (RS)",font=20).grid(row=15, column=4)
tk.Label(master, fg="blue",text=" Discount (RS)",font=20).grid(row=16, column=4)
tk.Label(master,fg="blue", text=" Grand Total (RS)",font=20).grid(row=18, column=4)

tk.Label(master,fg="blue", text=" Address ",font=20).grid(row=16, column=1)
tk.Label(master,fg="red", text="12/5 Sector ",font=20).grid(row=15, column=2)
tk.Label(master,fg="red", text="Gopalpura By Pass ",font=20).grid(row=16, column=2)
tk.Label(master,fg="red", text="Jaipur (Raj)",font=20).grid(row=17, column=2)

tk.Label(master,fg="orange", text="Thank You",font=20).grid(row=15, column=3)
tk.Label(master,fg="orange", text="For Visitng",font=20).grid(row=16, column=3)
tk.Label(master,fg="orange", text="Our Shop",font=20).grid(row=17, column=3)

e1.grid(row=3, column=2)
e2.grid(row=4, column=2)
e3.grid(row=3, column=5)
e4.grid(row=4, column=5)

e5.grid(row=8, column=2)
e6.grid(row=9, column=2)
e7.grid(row=10, column=2)
e8.grid(row=11, column=2)
e9.grid(row=12, column=2)

e10.grid(row=8, column=3)
e11.grid(row=9, column=3)
e12.grid(row=10, column=3)
e13.grid(row=11, column=3)
e14.grid(row=12, column=3)

e15.grid(row=8, column=4)
e16.grid(row=9, column=4)
e17.grid(row=10, column=4)
e18.grid(row=11, column=4)
e19.grid(row=12, column=4)

button1 = tk.Button(master, text="SUBMIT",font=20, bg="white",fg="red", command=display)
button1.place(x=710,y=600)


tk.Label(master,font=20).grid(row=5, column=1)
tk.Label(master,font=20).grid(row=6, column=1)
tk.Label(master,font=20).grid(row=0, column=1)
tk.Label(master,font=20).grid(row=1, column=1)
tk.Label(master,font=20).grid(row=2, column=1)
tk.Label(master,font=20,text="                                       ").grid(row=3, column=0)
tk.Label(master,font=20).grid(row=4, column=1)
tk.Label(master,font=20).grid(row=13, column=1)
tk.Label(master,font=20).grid(row=17, column=1)


master.mainloop()