from tkinter import Tk, Button, StringVar, Entry, IntVar


def click_btn():
    sum = x.get()+y.get()
    message.set(sum)

def click_btn1():
    btn1.config(text = "press")

if __name__ == '__main__':
    win = Tk()
    btn_text = StringVar()
    btn_text.set("button")
    win.title(btn_text.get())
    win.geometry("400x500")

    message = StringVar()
    x = IntVar()
    y = IntVar()

    x_entry = Entry(textvariable=x)
    x_entry.pack()
    y_entry = Entry(textvariable=y)
    y_entry.pack()
    m_entry = Entry(textvariable=message)
    m_entry.pack()
    btn = Button(textvariable = btn_text, command=click_btn )
    btn.pack()

    btn1 = Button(text="text", command=click_btn1)
    btn1.pack()
    win.mainloop()