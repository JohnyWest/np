from tkinter import *

root = Tk()
root.title('Заметочки')
root.geometry('700x800')
root.iconbitmap('Ico.ico')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

#Settings of a text field
text_field = Text(f_text, 
                  bg='gray', 
                  fg='white',
                  padx=15,
                  pady=15,
                  wrap=WORD,
                  insertbackground='brown',
                  selectbackground='lime',
                  spacing3=15,
                  width=10
                  )
text_field.pack(expand=1, fill=BOTH, side='left')
#Adding a scrollbar
scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)


#Loop
root.mainloop()
