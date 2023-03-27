from tkinter import *

root = Tk()
root.title('Заметочки')
root.geometry('700x800')
root.iconbitmap('Ico.ico')



def change_fonts(fontss):
    text_field['font'] = fonts[fontss]['text_bg']
    
    
    
#Раздел меню
main_menu = Menu(root)

##Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть')
root.config(menu=main_menu)

root.config(menu=main_menu)

##Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная тема')
view_menu_sub.add_command(label='Светлая тема')
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

###Шрифт
font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Roboto', command=lambda: change_fonts('Roboto'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('Times New Roman'))
view_menu.add_cascade(label='Шрифт', menu=font_menu_sub)
root.config(menu=view_menu)

#Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)

# Фрейм
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)



fonts = {
    'Arial':{
        'font': 'Arial 14 bold'
    },
    'Roboto':{
        'font': ('Roboto', 14, 'bold'
        )
    },
    'Times New Roman':{
        'font': ('Times New Roman', 14, 'bold'
        )
    }
}



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
                  width=10,
                  font='Arial 14 bold'                
                  )
text_field.pack(expand=1, fill=BOTH, side='left')
#Adding a scrollbar
scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)


#Loop
root.mainloop()
