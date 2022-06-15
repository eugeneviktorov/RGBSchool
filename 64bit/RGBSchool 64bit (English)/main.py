from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('RGBSchool')
root.geometry('900x506+10+10')
root.resizable(False, False)
root['bg'] = '#ffffff'
root.call('wm', 'attributes', '.', '-topmost', '1')
photo=tk.PhotoImage(file='./Logo1.png')
root.iconphoto(False, photo)


tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Home")
tab_control.add(tab2, text='Content')
tab_control.add(tab3, text='Head 1.1')
tab_control.add(tab4, text='Head 1.2')
tab_control.add(tab5, text='Head 2.1')
tab_control.add(tab6, text='Head 2.2')

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

lbl22 = Button(tab2, text='Head 1.1: Vector graphics',bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab1, relief=FLAT, width=470, anchor='w', padx=10)
lbl22.pack()

lbl222 = Button(tab2, text='Head 1.2: Practice in vector graphics', bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab2, relief=FLAT, width=470, anchor='w', padx=10)
lbl222.pack()

lbl2222 = Button(tab2, text='Head 2.1: Raster graphics', bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab3, relief=FLAT, width=470, anchor='w', padx=10)
lbl2222.pack()

lbl22222 = Button(tab2, text='Head 2.2: Raster graphics practice', bg='#ffffff', fg='#000000',activebackground='#ffffff', activeforeground='#000000', font=('Arial',16), command=lasttab4, relief=FLAT, width=470, anchor='w', padx=10)
lbl22222.pack()

lbl2 = Label(tab2, text="", bg='white', fg='black',width=470, height=100, anchor='w', padx=10, pady=10)
lbl2.pack()



lbl3 = Label(tab3, text="Head 1.1: Vector graphics", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl3.pack()

lbl3 = Label(tab3, text="A vector image is a graphical object built \nfrom geometric primitives such as points, \nlines, splines, and polygons. \n \n"
                        "For professional work with vector \ngraphics, we take 'Figma' program. \nWith it, you can create many professional \ngraphic objects. \n \n"
                        "To get started, register on the site \n“figma.com”\n \n \n ", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=20, anchor='w', padx=10, pady=40)
lbl3.pack()

our_image=PhotoImage(file="./Photo1.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab3)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=385, y=50)



lbl4 = Label(tab4, text="Head 1.2: Practice in vector graphics", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl4.pack()

lbl4 = Label(tab4, text="The purpose of practical work on vector \ngraphics: study of the ‘Figma’ program. \nUsed for illustrations icons, logos and \ntechnical drawings, but complex \nto reproduce photorealistic images. \n \n"
                        "After registration, we create a new \nproject (New design file). \nAfter loading the project, you can create \nvector graphics.\n \n"
                        "And to begin with, we will create an object, and also look at how keyboard shortcuts work. \n \n"
                        "In the image, you can see the toolbar at the top. Select the object highlighted in blue.\n"
                        "And create a square by holding the shift button. Using the palette on the panel on the right, you \n"
                        "can set the color and transparency.", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=30, anchor='w', padx=10, pady=0)
lbl4.pack()

our_image=PhotoImage(file="./Photo2.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab4)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=350, y=50)



lbl5 = Label(tab5, text="Head 2.1: Raster graphics", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl5.pack()

lbl5 = Label(tab5, text="A raster image is an image that is a grid \n(mosaic) of pixels - colored dots, usually \nrectangular: on a monitor, paper and other \ndisplay devices.\n \n "
                        "To work with raster graphics, we need \nphotoshop. But there is a free version of \n'photoshop' (online-fotoshop.ru) \nFor beginners, this service will help in the \nfuture to master 'photoshop' itself. \n \n \n \n", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=0, anchor='w', padx=10, pady=80)
lbl5.pack()

our_image=PhotoImage(file="./Photo3.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab5)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=385, y=50)



lbl6 = Label(tab6, text="Head 2.2: Raster graphics practice", bg='white', fg='black',justify=LEFT, font=('Arial',18, 'bold'), width=470, height=0, anchor='w', padx=10, pady=10)
lbl6.pack()

lbl6 = Label(tab6, text="The purpose of practical work on raster \ngraphics: the study of the program \n‘Photoshop’. With the help of computer \ngraphics, you can already work on web \ndesign, video games, 3D printing, \nanimations, VR, visualization, special \neffects for cinema, etc. today. \n \n"
                        "Create a file to work with. \n‘No templates’.\n \n"
                        "And add any photo with the object. \nThen press 'Enter'. \n \n"
                        "And selecting the magic wand tool (shown in the image) on the toolbar on the left side. Select an \nobject. select an object. \n \n"
                        "After selecting the object, press (ctrl c) and then (ctrl v). And on the right side, you can turn off layers. Select the layer you want and turn it off. \n Your object is cut out.", bg='white', fg='black',justify=LEFT, font=('Arial',14), width=470, height=25, anchor='w', padx=10, pady=0)
lbl6.pack()

our_image=PhotoImage(file="./Photo4.png")
our_image=our_image.subsample(2,2)
our_label=Label(tab6)
our_label.image=our_image
our_label['image']=our_label.image
our_label.place(x=350, y=70)



tab_control.pack(expand=1, fill='both')
root.mainloop()