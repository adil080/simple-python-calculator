from tkinter import *

txt_pad = [
   #("0")|("1")|("2")|("3")
   # (------------)             #(0)
    ("c"),("("),(")"),("/"),    #(1)
    ("7"),("8"),("9"),("*"),    #(2)
    ("4"),("5"),("6"),("-"),    #(3)
    ("1"),("2"),("3"),("+"),    #(4)
    ("00"),("0"),("."),("=")    #(5)
]

i = 0
gridx = 4
gridy = 6
w = 6
h = round(w/2)
clear = False

def read_bnt(bnt):
    global clear
   
    if bnt == "c":
        ent_field.delete(0,END)
        ent_field.insert(END, "0")

    elif bnt == "=":
        clear = True
        result = f" = {eval(ent_field.get())}"
        ent_field.insert(END, result)

    else:
        if clear == True or ent_field.get() == "0":
            clear = False
            ent_field.delete(0,END)

        ent_field.insert(END, bnt)



win = Tk()
win.title("Calculator")

ent_field = Entry(width=w*(gridy-1))
ent_field.insert(END, "0")
ent_field.grid(row=0, column=0, columnspan=gridy)


for y in range(1 , gridy):
    for x in range(0 , gridx):
        bnt_pad = Button(
            text = str(txt_pad[i]),
            width=w,
            height=h,
            relief="raised",
            command= lambda b = txt_pad[i] : read_bnt(b)
            )
        
        i += 1
        bnt_pad.grid(column=x, row=y)

win.mainloop()