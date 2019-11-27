"""
based from programming python book by mark lutz 4th ed
"""
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename, SaveAs
from tkinter.messagebox import askokcancel
import os

class TextEditor(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.grid(sticky=NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.font = ('consolas', 10, 'normal')
        self.bg = '#000000'
        self.fg = '#80FA7B'
        self.insert_bg = '#FFFFFF'
        self.ftypes = [('Python file', '.py'), ('Text file', '.txt')]
        self.curr_cwd = os.getcwd()
        
        self.root = parent
        self.make_menu()
        self.make_widgets()
        self.text.focus()
        
        
    def make_widgets(self):
        vbar = Scrollbar(self)
        hbar = Scrollbar(self, orient='horizontal')
        text = Text(self, relief=SUNKEN, padx=5, pady=5, wrap='none')
        self.text = text
        
        text.grid(row=0, column=0, sticky=NSEW)
        vbar.grid(row=0, column=1, sticky=NSEW)
        hbar.grid(row=1, column=0, sticky=NSEW)
        
        vbar.config(command=text.yview)
        hbar.config(command=text.xview)
        text.config(yscrollcommand=vbar.set)
        text.config(xscrollcommand=hbar.set)
        text.config(font=self.font, bg=self.bg, fg=self.fg, insertbackground=self.insert_bg)
        
        
    def make_menu(self):
        top = Menu(self.root)
        self.root.config(menu=top)
        file = Menu(top)
        file.add_command(label='Open File', command=lambda: self.on_open())
        file.add_command(label='Save File', command=lambda: self.on_save())
        file.add_command(label='Quit', command=lambda: self.on_quit())
        top.add_cascade(label='Menu', menu=file, underline=0)
        
        
    def on_open(self):
        filename = askopenfilename(initialdir=self.curr_cwd, filetypes=self.ftypes)
        if filename:
            self.text.delete("1.0", "end")
            alltext = open(filename, 'r').readlines()
            for line in alltext:
                self.text.insert("end", str(line))
                self.text.see("end")
        
        
    def on_save(self):
        filename = asksaveasfilename(initialdir= os.getcwd())
        if filename:
            alltext = self.text.get('1.0', END+'-1c')
            open(filename, 'w').write(alltext)
    
    
    def on_quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')
        if ans: self.quit()
        
        
if __name__ == '__main__':
    root = Tk()
    root.title("JocoGum's Text Editor")
    root.iconbitmap('guitar.ico')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    editor = TextEditor(root)
    editor.mainloop()