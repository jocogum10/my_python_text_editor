"""
based from programming python book by mark lutz 4th ed
"""
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
        self.ftypes = [('Python file', '.py')]
        self.curr_cwd = os.getcwd()
        
        self.root = parent
        self.make_menu()
        self.make_widgets()
        self.text.focus()
        self.filename = ''
        
        
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
        file.add_command(label='Run Code', command=lambda: self.on_run_code())
        file.add_command(label='Quit', command=lambda: self.on_quit())
        top.add_cascade(label='Menu', menu=file, underline=0)
        
        
    def on_open(self):
        filename = filedialog.askopenfilename(initialdir=self.curr_cwd, filetypes=self.ftypes)
        if filename:
            self.filename = filename
            self.text.delete("1.0", "end")
            alltext = open(filename, 'r').readlines()
            for line in alltext:
                self.text.insert("end", str(line))
                self.text.see("end")
        
        
    def on_save(self):
        filename = filedialog.asksaveasfilename(initialdir= self.curr_cwd, defaultextension='.py', initialfile='*.py')
        if filename:
            self.filename = filename
            alltext = self.text.get('1.0', END+'-1c')
            open(filename, 'w').write(alltext)
            
    
    def on_run_code(self):
        if self.filename:
            os.system('cmd /c "py {0}"'.format(self.filename))
        else:
            messagebox.showerror('Error Run Command','No Open/Saved File', detail='Open or Save a file first')
    
    
    def on_quit(self):
        ans = messagebox.askokcancel('Verify exit', 'Really quit?')
        if ans: self.quit()
        
        
if __name__ == '__main__':
    root = Tk()
    root.title("JocoGum's Python Text Editor")
    #root.iconbitmap('guitar.ico')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    editor = TextEditor(root)
    editor.mainloop()