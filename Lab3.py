import tkinter 

def hello(args: str)->None:
    global label_output
    label_output.config(text="")
    label_output.config(text = "Good " + args + " Molly.")
    

def main()->None:
    menu = tkinter.Tk()
    menu.title("Lab 3")
    menu.geometry("300x100")
    button1 = tkinter.Button(menu, text="Morning", command=lambda: hello("Morning"))
    button2 = tkinter.Button(menu, text="Afternoon", command=lambda: hello("Afternoon"))
    global label_output 
    label_output = tkinter.Label(text="")
    button1.pack()
    button2.pack()
    label_output.pack()
    menu.mainloop()
    
if __name__ == "__main__":
    main()