from tkinter import Tk, Label, Button

#Window with a label and two buttons

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title('A simple GUI')
        
        self.label = Label(master, text='This is our first GUI')
        self.label.pack()
        
        self.greet_button = Button(master, text='Greet', command=self.greet)
        self.greet_button.pack()
        
        self.wow_button = Button(master, text='Wow', command=self.wow)
        self.wow_button.pack()
        
        self.close_button = Button(master, text='Close', command=master.quit)
        self.close_button.pack()
        
    def greet(self):
        print("Greetings!")
    
    def wow(self):
        print("Wow, you're amazing AND beautiful. Keep up the good work.")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()