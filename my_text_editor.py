"""
based from programming python book by mark lutz 4th ed
"""
from tkinter import *
from tkinter.filedialog import asksaveasfilename

class TextEditor(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.grid(sticky=NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.font = ('consolas', 12, 'normal')
        self.bg = '#000000'
        self.fg = '#80FA7B'
        self.insert_bg = '#FFFFFF'
        
        self.root = parent
        self.makemenu()
        self.makewidgets()
        self.text.focus()
        
    def makewidgets(self):
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
        
    def makemenu(self):
        top = Menu(self.root)
        self.root.config(menu=top)
        file = Menu(top)
        file.add_command(label='Save File', command=(lambda: self.on_save()), underline=0)
        top.add_cascade(label='File', menu=file, underline=0)
        
    def on_save(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.text.get('1.0', END+'-1c')
            open(filename, 'w').write(alltext)
        
if __name__ == '__main__':        
    root = Tk()
    root.title("JocoGum's Text Editor")
    root.iconbitmap('guitar.ico')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    editor = TextEditor(root)
    editor.mainloop()