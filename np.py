from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def change_fonts(fontss):
    text_field['font'] = fonts[fontss]['font']
    
def change_theme(theme):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']

def np_openfile():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*txt'), ('Все файлы', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())

def np_savefile():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()

def np_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()



root = Tk()
root.title('Заметочки')
root.geometry('700x800')
root.iconbitmap('Ico.ico')
 
#Раздел меню
main_menu = Menu(root)

##Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=np_openfile)
file_menu.add_command(label='Сохранить', command=np_savefile)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=np_exit)
root.config(menu=main_menu)


##Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная тема', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Светлая тема', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

###Шрифт
font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('Comic Sans MS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('Times New Roman'))
view_menu.add_cascade(label='Шрифт', menu=font_menu_sub)
root.config(menu=view_menu)

#Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)

# Фрейм
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)


view_colors = {
    'dark': {
        'text_bg': '#121212',
        'text_fg': 'white',
        'cursor': 'brown',
        'select_bg': 'lime'
    },
    'light': {
        'text_bg': 'white',
        'text_fg': 'black',
        'cursor': '#A5A5A5',
        'select_bg': '#FAEEDD'
    }
}
fonts = {
    'Arial':{
        'font': 'Arial 14 bold'
    },
    'Comic Sans MS':{
        'font': ('Comic Sans MS', 14, 'bold'
        )
    },
    'Times New Roman':{
        'font': ('Times New Roman', 14, 'bold'
        )
    }
}



#Settings of a text field
text_field = Text(f_text, 
                  bg='#121212', 
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
