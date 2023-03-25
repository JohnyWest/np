from tkinter import *

root = Tk()
root.title('Заметочки')
root.geometry('700x800')
root.iconbitmap('Ico.ico')

#Раздел меню
main_menu = Menu(root)

#Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть')
root.config(menu=main_menu)

root.config(menu=main_menu)

#Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_command(label='Открыть')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

#Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)


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
