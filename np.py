from tkinter import *

root = Tk()
root.title('Заметочки')
root.geometry('700x800')
root.iconbitmap('Ico.ico')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_field = Text(f_text, bg='gray', fg='white')
text_field.pack(expand=1, fill=BOTH, side='left')


root.mainloop()
