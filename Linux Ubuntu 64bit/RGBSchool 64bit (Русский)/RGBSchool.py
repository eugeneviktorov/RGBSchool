from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('RGBSchool')
root.geometry('900x506+10+10')
root.resizable(False, False)
root['bg'] = '#ffffff'
root.call('wm', 'attributes', '.', '-topmost', '1')
photo=tk.PhotoImage(file='Logo1.png')
root.iconphoto(False, photo)


tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Главная")
tab_control.add(tab2, text='Содержание')
tab_control.add(tab3, text='Глава 1.1')
tab_control.add(tab4, text='Глава 1.2')
tab_control.add(tab5, text='Глава 2.1')
tab_control.add(tab6, text='Глава 2.2')

def lasttab1():
    tab_control.select(tab3)

def lasttab2():
    tab_control.select(tab4)

def lasttab3():
    tab_control.select(tab5)

def lasttab4():
    tab_control.select(tab6)



lbl1 = Label(tab1)
lbl1.grid()

our_image=PhotoImage(file="Home.png")
our_image=our_image.subsample(1,1)
our_label=Label(tab1)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=0, y=-25)



lbls2 = Label(tab2, text="", bg='white', fg='black',width=470, height=0, anchor='w', padx=10, pady=10)
lbls2.pack()

lbl22 = Button(tab2, text='Глава 1.1: Векторная графика',bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab1, relief=FLAT, width=470, anchor='w', padx=10)
lbl22.pack()

lbl222 = Button(tab2, text='Глава 1.2: Практика по векторной графике', bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab2, relief=FLAT, width=470, anchor='w', padx=10)
lbl222.pack()

lbl2222 = Button(tab2, text='Глава 2.1: Растровая графика', bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab3, relief=FLAT, width=470, anchor='w', padx=10)
lbl2222.pack()

lbl22222 = Button(tab2, text='Глава 2.2: Практика по растровой графике', bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab4, relief=FLAT, width=470, anchor='w', padx=10)
lbl22222.pack()

lbl2 = Label(tab2, text="", bg='white', fg='black',width=470, height=100, anchor='w', padx=10, pady=10)
lbl2.pack()



lbl3 = Label(tab3, text="Глава 1.1: Векторная графика", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl3.pack()

lbl3 = Label(tab3, text="Векторное изображение - это \nграфический объект, построенный из \nгеометрических примитивов, таких как \nточки, линии, сплайны и многоугольники. \n \n"
                        "Для проффесиональной работы с \nвекторной графикой, мы берём \nпрограмму 'Figma'. \nС помощью неё можно создавать многие \nпроффесиональные графические \nобъекты. \n \n"
                        "Сначала зарегистрируйтесь на сайте \n'figma.com' \n \n \n ", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=20, anchor='w', padx=10, pady=40)
lbl3.pack()

our_image=PhotoImage(file="Photo1.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab3)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=385, y=50)



lbl4 = Label(tab4, text="Глава 1.2: Практика по векторной графике", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl4.pack()

lbl4 = Label(tab4, text="Цель практической работы по \nвекторной графике: изучение \nпрограммы ‘Figma’. \nИспользуется для иллюстраций, \nиконок, логотипов и технических \nчертежей, но сложна для \nвоспроизведения фотореалистичных \nизображений. \n \n"
                        "После регистрации создадим новый \nпроект (New design file). \nПосле загрузки проекта можно \nсоздавать векторную графику. \n \n"
                        "И для начала мы создадим объект, и также рассмотрим как работают сочетания клавиш. \n \n"
                        "На изображении вы можете увидеть панель инструментов сверху, выберете объект который \nвыделен голубым цветом. И создайте квадрат зажав кнопку 'shift'. \n"
                        "С помощью палитры на панели справа, вы можете задать цвет и прозрачность.", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=30, anchor='w', padx=10, pady=0)
lbl4.pack()

our_image=PhotoImage(file="Photo2.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab4)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=350, y=50)



lbl5 = Label(tab5, text="Глава 2.1: Растровая графика", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl5.pack()

lbl5 = Label(tab5, text="Растровое изображение - это, \nизображение, представляющее собой \nсетку (мозаику) пикселей - цветных точек, \nобычно прямоугольных: на мониторе, \nбумаге и других отображающих \nустройствах. \n \n"
                        "Для работы с растровой графикой нам \n'понадобится photoshop'. \nНо есть бесплатная версия photoshop \n(online-fotoshop.ru) \n \n"
                        "Для новичков данный сервис поможет \nв будущем освоить уже сам 'photoshop'. \n \n \n", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=0, anchor='w', padx=10, pady=40)
lbl5.pack()

our_image=PhotoImage(file="Photo3.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab5)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=385, y=50)



lbl6 = Label(tab6, text="Глава 2.2: Практика по Растровой графике", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl6.pack()

lbl6 = Label(tab6, text="Цель практической работы по \nрастровой графике: изучение \nпрограммы ‘Photoshop’.С помощью \nкомпьютерной графики уже сегодня \nможно работать над веб-дизайном, \nвидеоиграми, 3D-печатью, \nанимациями, VR, визуализацией, \nспецэффектами для кино и т. д. \n \n"
                        "Создайте файл для работы. \n'Без шаблонов'. \n \n"
                        "И добавьте любую фотографию с \nобъектом. После нажмите 'Enter'. \n \n"
                        "И выбрав инструмент волшебная палочка, (показано на изображении) на панели с инструментами \nс левой стороны. Выделите объект. \n"
                        "После выделения объекта, нажмите (ctrl c) и затем (ctrl v). И справой стороны вы можете \nотключать слои. Выберете нужный вам слой и отключите его. Ваш объект вырезан.", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=25, anchor='w', padx=10, pady=0)
lbl6.pack()

our_image=PhotoImage(file="Photo4.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab6)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=330, y=70)



tab_control.pack(expand=1, fill='both')
root.mainloop()