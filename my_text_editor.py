"""
based from programming python book by mark lutz 4th ed
"""
from tkinter import *

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
        
        self.makewidgets()
        
    def makewidgets(self):
        vbar = Scrollbar(self)
        hbar = Scrollbar(self, orient='horizontal')
        text = Text(self, relief=SUNKEN, padx=5, pady=5, wrap='none')
        
        text.grid(row=0, column=0, sticky=NSEW)
        vbar.grid(row=0, column=1, sticky=NSEW)
        hbar.grid(row=1, column=0, sticky=NSEW)
        
        vbar.config(command=text.yview)
        hbar.config(command=text.xview)
        text.config(yscrollcommand=vbar.set)
        text.config(xscrollcommand=hbar.set)
        text.focus()
        
        text.config(font=self.font, bg=self.bg, fg=self.fg, insertbackground=self.insert_bg)
        
        
if __name__ == '__main__':        
    root = Tk()
    root.title("JocoGum's Text Editor")
    root.iconbitmap('guitar.ico')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    editor = TextEditor(root)
    editor.mainloop()