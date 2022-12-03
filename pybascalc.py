import tkinter

window = tkinter.Tk()
window.geometry("451x556")
window.title("Calculator")
window.configure(background="#37373b")
window.resizable(0, 0) 

resulta = tkinter.Label(window,width=34, height=4, text="", font=("Helvetica 16 bold"), background="#37373b", foreground="#03fc66")
resulta.pack()

equation = ""
def show(value):
    global equation
    equation+=value
    resulta.config(text=equation)

def clear():
    global equation
    equation = ""
    resulta.config(text=equation)

def calc():
    global equation
    global result
    result = ""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="MATHS OR INPUT ERROR"
            equation=""
    resulta.config(text=result)

button1 = tkinter.Button(window, text="1", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("1")).place(x=0,y=373)
button2 = tkinter.Button(window, text="2", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("2")).place(x=113,y=373)
button3 = tkinter.Button(window, text="3", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("3")).place(x=226,y=373)
button4 = tkinter.Button(window, text="4", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("4")).place(x=0,y=282)
button5 = tkinter.Button(window, text="5", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("5")).place(x=113,y=282)
button6 = tkinter.Button(window, text="6", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("6")).place(x=226,y=282)
button7 = tkinter.Button(window, text="7", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("7")).place(x=0,y=191)
button8 = tkinter.Button(window, text="8", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("8")).place(x=113,y=191)
button9 = tkinter.Button(window, text="9", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("9")).place(x=226,y=191)
button0 = tkinter.Button(window, text="0", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("0")).place(x=0,y=465)

buttonadd = tkinter.Button(window, text="+", background="#e1e2e3", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("+")).place(x=339,y=465)
buttonsub = tkinter.Button(window, text="-", background="#e1e2e3", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("-")).place(x=339,y=373)
buttonmult = tkinter.Button(window, text="×", background="#e1e2e3", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("*")).place(x=339,y=282)
buttondiv = tkinter.Button(window, text="÷", background="#e1e2e3", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show("/")).place(x=339,y=191)

buttondec = tkinter.Button(window, text=".", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: show(".")).place(x=113,y=465)

buttonequal = tkinter.Button(window, text="=", background="#e1e2e3", font=("Helvetica 17 bold"), foreground="black", height=2, width=6, padx=10, pady=10, command=lambda: calc()).place(x=226,y=465)

buttonclear = tkinter.Button(window, text="C", background="#f27b0c", font=("Helvetica 17 bold"), foreground="black", height=2, width=14, padx=10, pady=10, command=lambda: clear()).place(x=1,y=99)

buttonexit = tkinter.Button(window, text="OFF", background="#b0b0b0", font=("Helvetica 17 bold"), foreground="black", height=2, width=14, padx=10, pady=10, command=window.destroy).place(x=226,y=99)

window.mainloop()
