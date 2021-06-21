
#import all components from tkinter
from tkinter import*

#import tkinter
#create the root window
'''
root = Tk()
root.title('my window')
root.geometry('400x300')
root.mainloop()


#program to create root window with some option

#create top level window


root = Tk()


#set window title
root.title('my window')

#set window size
root.geometry('400x300')

#set window icon
root.wm_iconbitmap('cat.gif')


#display window and wait for any events
root.mainloop()


from tkinter import font

root = Tk()

#get all the supported font families

list_fonts = list(font.families())

#dis_lay them
print(list_fonts)


#colors used directly by mention their name- blue, red, black

#containers

# container is a component that is used as a place where drawings 
#or widgets can be displayed.
#two imp container

#canvas
#draw shapes like lines, curves, arcs and circles

#frames
#used to diplay buttons, check buttons or menus

#c=canvas(root, bg='blue', height=500, width=600, cursor='pencil')

#c is the canvas class object
#root is the name of the parent window
#bg= background color
#pixel  1360*768

#cursor represent the shape of the cursor
#arrow, box spiral, center ptr, cirlce, clock,cross, mouse, penicl
#plus, star, umbrella, watch

#once the canvas is created, it should be added to the root window.
#then only it will be visible by using pack() method
#c.pack()

#after canvas is created, we can draw any shapes on teh canvas
#id=c.create_oval(100, 100, 400, 300, width=5, fill='yellow', 
#outline='red', activefill='green')

#this create an oval in the rectangular area
#top coordinates (100,100)
#bottom lower coordinates (400,300)
#fill clor to fill
#outline color to be used for border
#active fill coor to be filled when mouse is placed on the oval

#create_polygon
#id=c.create_polygon(10, 10, 200, 200, 300, 200, width=3, fill='green', 
#outline='red', activefill='lightblue')


#create_rectangle
#id=c.create_rectangle(500, 200, 700, 600, width=2, fill='gray', 
#outline='black', activefill='yellow')

#create_text
#id=c.create_text(500, 100, text='MY CANVAS', font=fnt, fill='yellow', 
# activefill='green')
#fnt=('Times', 40, 'bold italic underline')


#GUI pROGRAM creation of various shapes in canvas.

#create root window
from tkinter import*
root=Tk()

#set window title
root.title('my window')

#create canvas as a child to root window
c = Canvas(root, bg='white',height=700, width=1200,cursor='pencil')

#create a line in the canvas
id=c.create_line(50, 50, 200, 50,200,100,50,100,50,50, width=4, fill='white')
#create an oval in the canvas

id=c.create_oval(100, 100, 400, 300, width=5, fill='yellow',outline='red', activefill='green')

#create a polygon
id=c.create_polygon(100, 100, 200, 200, 300, 200, width=3, fill='green',outline='red', activefill='lightblue')

#create a rectangle
id=c.create_rectangle(500, 200, 700, 600, width=2, fill='gray',outline='black', activefill='yellow')

#create some text in the canvas
fnt=('Times', 40, 'bold italic underline')
id=c.create_text(500, 100, text='python programming', font=fnt, fill='yellow',activefill='green')
c.pack()
root.mainloop()


#important shapes is arc
#id=c.create_arc(100, 100, 400, 300, width=3, start=270, 
#extent=180, outline='red', style='arc')
#arc start 270 degree nd extend for another 180 degree
#450-360=90



#create root window
root=Tk()

#create canvas as a child to root window

c=Canvas(root, bg='white', height=700,width=1200)

# create arcs in the canvas

id=c.create_arc(100, 100, 400, 300, width=3, start=270, extent=180, outline='red', style='arc')

id=c.create_arc(500, 100, 800, 300, width=3, start=90, extent=180, outline='red', style='arc')

id=c.create_arc(100, 400, 400, 600, width=3, start=0, extent=180, outline='blue', style='arc')

id=c.create_arc(500, 400, 800, 600, width=3, start=180, extent=180, outline='blue', style='arc')

id=c.create_arc(900, 400, 1200, 600, width=3, start=90, extent=90, outline='black', style='arc')

#add canvas to the root
c.pack()
root.mainloop()



#pie slice, chord
root=Tk()

#create canvas as a child to root window

c=Canvas(root, bg='white', height=700,width=1200)

# create arcs in the canvas

id=c.create_arc(100, 100, 400, 300, width=3, start=270, extent=180,
                outline='red', style='arc')

id=c.create_arc(10, 50, 240, 210, width=3, start=90, extent=180,
                outline='red', style='chord')

id=c.create_arc(300, 500, 600, 800, width=3, start=90, extent=90,
                outline='black', style='pieslice')

c.pack()

root.mainloop()

'''
#we can display an image in canvas with the help of 
#create_image() method P

#file1=PhotoImage(file='image.jpg')
#id = c.create_image(500, 200, anchor=NE, image=file1, activeimage=file2)

from tkinter import*
root=Tk()
#create canvas as a child to root window

c=Canvas(bg='white', height=700,width=1200)

file1=PhotoImage(file="cat.gif")
file2=PhotoImage(file="dog.gif")

c.create_image(500, 200, anchor=NE, image=file1, activeimage=file2)
#c.create_image(500, 200, anchor=NE, image=file1
c.pack()
root.mainloop()
'''
#program to display a frame in the root window

from tkinter import*

root=Tk()
root.title('my frame')

f=Frame(root, height=400, width=500, bg='yellow', cursor='cross')

f.pack()

root.mainloop()


#Widget
#widget is a gui compoent  that is displayed on the screen and can perform a task as desired by the user
#we create widget as object. push button is a widget, is nothing but object of button class
#once the widget is create, it should be added to canvas or frame

button
label
message
text
scrollbar
checkbutton
radiobutton
entry
spinbox
listbox
menu

#working takes four steps:

#first
# create the widget, suppose we want to create the push button
#b=Button(f, text='my button')
#f is the object of the frame

#second
#when user interact with widget, he will generate an event
#clikcing a push button is an event
#such event should be handle by writing functiond or routines.
#there functions are called in response to the event.
#hence they called 'calback handlers' or event handlers
#ex= press the enter button, right click the mouse.

#def button(self):
   # print('you click me')

#third
#when user press push button, clicked event should be linked with event handler function
#then only the button widget will appear as if it is performing some task
#b.bind('<Button-1>', button)

#b represent the push button
#<button-1> indicate the left mouse button
#when user press the left button the buttonclick function is called as these are linked by bind() method

#four
#these event are continously monitored by our program with the help of a loop called 'event loop'
#root.mainloop()

from tkinter import*
def buttonclick(self):
    print('you have click me')

root=Tk()

#create frame

f=Frame(root, height=200, width=300)

#let hte frame wii not shrink
#f.propagate(0)

#attach frame with root window
f.pack()

b=Button(f, text="my button", width=15, height=2, bg='yellow',
         fg='blue', activebackground='green', activeforeground='red')

b.pack()
b.bind('<Button-1>', buttonclick)
root.mainloop

from tkinter import*
class mybutton:
    
    def __init__(self, root):
        #create a frame as child to root window
        self.f=Frame(root, height=200, width=300)
        #let the frame will not shrink
        self.f.propagate(0)
        
        #attch the frame to root window
        self.f.pack()
        
        #create a push button as child to frame and bind it to button click method
        self.b=Button(self.f, text='my button', width=15, height=2,
                      bg='yellow', fg='blue', activebackground='green',
                      activeforeground='red', command=self.buttonclick)
        
        #attach button to the frame
        self.b.pack()
        
    def buttonclick(self):
        print('you gone')
        
root = Tk()
#create an object to my button class
mb = mybutton(root)
root.mainloop()


#when we create several button we need to know which button is clicked by the user
#we have to call event handler function by passing some argument
#self.b1=Button(self.f, text='Red', width=15, height=2, command=lambda: self.buttonclick(1))
#we creatin the push button b1
#we use the lambda expression to pass the argument 1 to the buttonclick() method


from tkinter import*
class mybutton:
    def __init__(self, root):
        #create a frame as child to root window
        self.f=Frame(root, height=400, width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        
        #attch the frame to root window
        self.f.pack()
        # create 3 push button and bind them to button click method and pass a number
        self.b1=Button(self.f, text='Red', width=15, height=2,
                       command=lambda: self.buttonclick(1))
        self.b2=Button(self.f, text='Green', width=15, height=2,
                       command=lambda: self.buttonclick(2))
        self.b3=Button(self.f, text='Blue', width=15, height=2,
                       command=lambda: self.buttonclick(3))

        # attach button to the frame
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

        #method to be called when the button is clicked
    def buttonclick(self, num):
        #set the background color of frame depending on the button clicked

        if num==1:
            self.f['bg']='red'
        if num==2:
            self.f['bg']='green'
        if num==3:
            self.f['bg']='blue'

#create root window
root = Tk()
#create an object to my button class
mb=mybutton(root)
#the root window handles the mouse click event
root.mainloop()

#arranging widgets in the frame

#pack layout manger
#grid layout manager
# place layout manager

#b.pack(fill=x)
#b.pack(fill=y)

#b1.pack(fill=y, padx=10, pady=15) occupy vertically , space x-axis 10px, y-axis 15px

#b1.pack(fill=x, padx=10, pady=15) occupy horizontally , space x-axis 10px, y-axis 15px

# pack() method can another option left, right, top, bottom
#default value is top

#b1.pack(side=LEFT, padx=10, pady=15) ALING TOwords left , space x-axis 10px, y-axis 15px

#b1.pack(side=RIGHT, padx=10, pady=15) ALING TOwords left , space x-axis 10px, y-axis 15px

#grid
#b1.grid(row=0, column=0, padx=10, pady=15)
#b1.grid(row=0, column=1, padx=10, pady=15)
#b1.grid(row=0, column=2, padx=10, pady=15)
#b1.grid(row=1, column=3, padx=10, pady=15)


#place

#b1.place(x=20, y=30, width=100, height=50) display at (20,30)
#b2.place(x=200, y=300, width=100, height=50) display at (200,300)


from tkinter import font

def buttonclick(self):
    print('hello')
root = Tk()
f=Frame(root, height=200, width=300)
f.propagate(0)
f.pack()
b=Button(f, text='red', width=15, height=2, bg='yellow', fg='blue',
         activebackground='green', activeforeground='red')
b1=Button(f, text='blue', width=15, height=2, bg='yellow', fg='blue',
          activebackground='green', activeforeground='red')
b2=Button(f, text='green', width=15, height=2, bg='yellow', fg='blue',activebackground='green', activeforeground='red')
b3=Button(f, text='yellow', width=15, height=2, bg='yellow', fg='blue',activebackground='green', activeforeground='red')

#b.pack(fill=Y, padx=10, pady=15)
#b1.pack(fill=X, padx=10, pady=15)
#b.pack(side=RIGHT, padx=10, pady=15)
#b1.pack(side=LEFT, padx=10, pady=15)

b.grid(row=0, column=0, padx=20, pady=15)
b1.grid(row=2, column=1, padx=10, pady=15)
b2.grid(row=0, column=2, padx=10, pady=15)
b3.grid(row=1, column=3, padx=10, pady=15)



#label widget
# represent constant text that is displayed inthe frame

#lbl=Label(f, text='welcome to python', width=20, height=2,
 #         font('courier', -30, bold underline), fg='blue', bg='yellow')


#program to display a label upon clicking a push button
from tkinter import*

class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.b1=Button(self.f, text='click me', width=15, height=2, command = self.buttonclick)

        #create another button that closes the rrot window upon clicking
        self.b2=Button(self.f, text='close', width=15, height=2, command = quit)

        #attach buttons to the frame

        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)

        #event handler method

    def buttonclick(self):
    #create label with some text
        self.lbl=Label(self.f, text='welcome to python', width=20, height=2,
                       font=('courier', -30, 'bold underline'), fg='blue', bg='yellow')

        #attach the label on the frame
        self.lbl.grid(row=2, column=0)

root=Tk()
mb=mybuttons(root)
root.mainloop()

#message widget

#m=Message(f, text='This is a message', width=200,
   #       font=('Roman', 20, 'bold italic'), fg='dark goldenrod')


#   program to display a message in the frame

from tkinter import*

class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()
        #create messsage
        self.m=Message(self.f, text='This is a message that has more than one line',
                       width=200,font=('Roman', 20, 'bold italic'), fg='dark goldenrod')
         #attach message to the frame

        self.m.pack(side=LEFT)

root=Tk()
mb=mybuttons(root)
root.mainloop()


#TEXT WIDGET
#t=Text(root,width=20, height=10, font=('Verdana', 14, 'bold'),
#fg='blue', bg='yellow, wrap=WORD')

#SCROLL WIDGET

#SCROLL BSR IS A WIDGET IS USEFUL TO SCROLL THEE TEXT IN ANTHER WIDGET
#TWO TYpE OF SCROLL BAR
#HORIZONTAL TO VERTICAL
#VIEW TEXT FROM LEFT TO RIGHT
#VERTICAL SCROLL BAR
#SCROLL THE TEXT FROM TOp TO BOTTOM
#CREATE SCROLL BAR CLASS

# h = Scrollbar(root, orient=Horizontal, bg='green', command=t.xview)

#h represent the scrollbar object

#h = Scrollbar(root, orient=vertical, bg='green', command=t.xview)

#after creating the scroll bar it shoud to be attach to the widgeet like text widget

#t.configure(xscrollcommand=h.set)

#xscrollcommand calls the set() method of horizontal scroll bar
#same way we can attach vertival

#t.configure(xscrollcommand=v.set)

#finally the scroll bar should be attached to the root window using pack() or grid()

#h.pack(side=BOTTOM, fill=X)
#v.pack(side=RIGHT,fill=Y)

from tkinter import*
class mybuttons:

    def __init__(self, root):

        #CREATE a text widget with 70 chars width and 15 lines height
        self.t=Text(root, width=70, height=15, wrap=NONE)

        #insert some text into the text widget
        for i in range(50):
            self.t.insert(END, 'THIS IS SOME TEXT')

        #ATTACH text widget to root window at the top
        self.t.pack(side=BOTTOM, fill=X)

        #CREATE horizontal scroll bar attach it to text widget

        self.h=Scrollbar(root, orient=HORIZONTAL,command=self.t.xview)

        #attach text widget to the horizantal scroll bar

        self.t.configure(xscrollcommand=self.h.set)

        #attach scroll to root window
        self.h.pack(side=BOTTOM, fill=X)
root=Tk()
mb=mybuttons(root)
root.mainloop()

#CHECKBUTTON WIDGET

#check button in the form of square shape
#when check button is selected a tick mark is displayed on the button

#c1=Checkbutton(f, bg='yellow', fg='green', font=('Georgia', 20, 'undeline'),
#text='java', variable=var1, command=display)

#variable rep. an object IntVar() class. 'command' represents the method to be called
#when user clicks the check button.

#var1= IntVar()

#when check button is clicked or selected the value of var1 will be 1
#otherwise it wiil be 0.

#to retrieve the value from var1 we should ise the get() method
#x= var1.get() # x value can be 0 or 1
from tkinter import*
class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        #create intvar class variables
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        #create check box and bind them to display method

        self.c1 = Checkbutton(self.f, bg = 'yellow', fg='green',
                              font=('Georgia', 20, 'underline'), text='java',
                              variable=self.var1, command=self.display)
        self.c2 = Checkbutton(self.f, bg = 'yellow', fg='green',
                              font=('Georgia', 20, 'underline'), text='python',
                              variable=self.var2, command=self.display)
        self.c3 = Checkbutton(self.f, bg = 'yellow', fg='green',
                              font=('Georgia', 20, 'underline'), text='.net',
                              variable=self.var3, command=self.display)
        #attach check boxes to the frame

        self.c1.place(x=50, y=200)
        self.c2.place(x=200, y=100)
        self.c3.place(x=350, y=100)

    def display(self):
        #retrieve the control variable values
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()

        #string is empty initially

        str=''
        #catch user choice

        if x==1:
            str+='java'
        if y==1:
            str+='python'
        if z==1:
            str+='.net'
            
        #display the user selection as a label
        lbl= Label(text=str, fg='blue').place(x=100, y=150, width=400, height=100)

        
root=Tk()
mb=mybuttons(root)
root.mainloop()


#RADIO BUTTON

#r1=Radiobutton(f, bg='yellow', fg='green', font=('Georgia', 20, 'underline'),
# text='Male', Variabel=var, value=1)

#var = IntVar()

class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        #create intvar class variables
        self.var = IntVar()

        self.r1=Radiobutton(self.f, bg='yellow', fg='green', font=('Georgia', 20, 'underline'),
                            text='Male', variable=self.var, value=1, command=self.display)
        self.r2=Radiobutton(self.f, bg='blue', fg='black', font=('Georgia', 20, 'underline'),
                            text='Female', variable=self.var, value=2, command=self.display)


        #attach radio buttons to the frame

        self.r1.place(x=50,y=100)
        self.r2.place(x=200,y=100)

    def display(self):
            #retrieve the control variable
        x=self.var.get()

            #string is empty initially

        str=''
            #catch user choice

        if x==1:
            str+= 'you selected: male'

        if x==2:
            str+= 'you selected: female'

        lbl = Label(text=str, fg='blue').place(x=50, y=150, width=200, height=20)
           
root=Tk()
mb=mybuttons(root)
root.mainloop()
'''
#entry widget

#e1=entry(f, width=25, fg='blue', bg='yellow',
#font=('Arial', 14),show='*')

#e1.bind('<return>', self. display)

#def display (self, event)
'''

class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        #labels

        self.l1=Label(text='First name:')
        self.l2=Label(text='last name')

        #create entry widget fro user name
        self.e1=Entry(self.f, width=25, fg='blue', bg='yellow',
                 font=('Arial', 14))

        #create entry widget for password, the text in widget
        #replace by *

        self.e2=Entry(self.f, width=25, fg='blue', bg='yellow',
                      font=('Arial', 14))

        #when user press enter, bind that event to display method

        self.e1.bind('<Return>', self.display)
        self.e2.bind('<Return>', self.display)

        #place labels and entry widgets in teh frame
        self.l1.place(x=50,y=100)
        self.l2.place(x=50,y=150)
        self.e1.place(x=200,y=100)
        self.e2.place(x=200,y=150)

    def display(self, event):
        str1=self.e1.get()
        str2=self.e2.get()

        #display the values using labels

        lbl1=Label(text='your name is :'+ str1).place(x=50, y=200)
        lbl2=Label(text='your password is :' +str2).place(x=50, y=220)
root=Tk()
mb=mybuttons(root)
root.mainloop()

#SpINBOX WIDGET

#S1= Spinbox(f, from_=5 to=15, textvariable=val1, width=15,
#fg='blue', bg='yellow', font=('Arial', 14, 'bold'))

#val1=IntVar()

#S2= Spinbox(f, values=('hyderabad', 'Delhi', 'kolkata', 'banglore'),
#textvariable=val1, width=15,fg='blue', bg='yellow', font=('Arial', 14, 'bold'))

#val2=StringVar()

#a.val1.get()
#s.val2.get()



class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.val1 =IntVar()
        self.val2=StringVar()

        self.s1= Spinbox(self.f, from_=5, to=15, textvariable=self.val1, width=15,
                    fg='blue', bg='yellow', font=('Arial', 14, 'bold'))

        self.s2= Spinbox(self.f, values=('hyderabad', 'Delhi', 'kolkata', 'banglore'),
                    textvariable=self.val2, width=15,fg='blue', bg='yellow',
                         font=('Arial', 14, 'bold'))
        self.b=Button(self.f, text='get values from spinboxes', command=self.display)

        self.s1.place(x=50, y=50)
        self.s2.place(x=50, y=100)
        self.b.place(x=50, y=150)


    def display(self):
        a= self.val1.get()
        s=self.val2.get()

        lbl1=Label(text='selected value: ' + str(a)).place(x=50,y=200)
        lbl2=Label(text='selected city: ' +s).place(x=50,y=220)
        

root=Tk()
mb=mybuttons(root)
root.mainloop()

#LISTBOX WIDGET

#single  we can select on eitem from all avilable list

#multiple

#lb = Listbox(f, font='Arial 12 bold', fg='blue', bg='yelloe', height=8,
#width=24, activestyle='underline', selectmode=MULTIPLE)

#ONCE THE LIST BOX CREATED
#WE SHOULD INSERT ITEMS using insert method

#lb.insert(0, 'univesity')
#lb.insert(1, 'college')

#to bind the listbox select event

#lb.bind('<<ListboxSelect>>', on_select)
#when the user select any items in teh list box, the method on_select() called

#def on_select(event):
#lst =[ ]
#know the indexes of the selected items
#indexes = lb.curselection()

#retrieve the items names depending on indexes
#append the items names to the list box

#for i in indexes:
#    lst.append(lb.get(i))

#program to create a list
class mybuttons:

    def __init__(self, root):

        self.f=Frame(root, height=400, width=700)
        self.f.propagate(0)
        self.f.pack()

        self.lbl=Label(self.f, text='click one or more of the univerity below:',
                       font='Calibri 14')
        self.lbl.place(x=50,y=50)
        
        self.lb = Listbox(self.f, font='Arial 12 bold', fg='blue', bg='yellow', height=8,
                     width=24, activestyle='underline', selectmode=MULTIPLE)
        self.lb.place(x=50, y=100)

        #using for loop items into list box

        for i in [ 'standford university','oxford univerity','texas univerity',
                   'cambridge university','university of california']:

            self.lb.insert(END, i)

        #bind the Listbox select event

        self.lb.bind('<<ListboxSelect>>', self.on_select)

        #create text box to display
        self.t=Text(self.f, width=40, height=6, wrap=WORD)
        self.t.place(x=300, y=100)

    def on_select(self, event):

        self.lst = [ ]

        indexes= self.lb.curselection()
        for i in indexes:
            self.lst.append(self.lb.get(i))

        #delet the previous content of the text box

        self.t.delete(0.0, END)
        #INSERT NEW CONTENTS INTO THE BOX

        self.t.insert(0.0, self.lst)


root=Tk()
mb=mybuttons(root)
root.mainloop()

#MENU WIDGET

#DISpLAY OpTIONS NEW, OpEN, SAVE...

#first create a menu bar
#menubar = Menu(root)

#menubar attach with root
#root.config(menu=menubar)

#create a menubar with group of items
#filemenu = menu(root, tearoff=0) tearoff for check items in menu if it is 1 no item dash line
#if 0 then contain menu items

#filemenu.add_command(label='New', command=donothing)

#add horizontal line as seperator
#filemenu.add_separator()

#after adding all menu items to filemenu object we should give it a neme and
#add it to menu bar using add_cascade(label='file', menu=filemenu)

from tkinter import*
class mymenudemo:
    def __init__(self, root):
        #create menubar
        self.menubar = Menu(root)

        #attach the menubar to the root window
        root.config(menu=self.menubar)

        #create file menu
        self.filemenu=Menu(root, tearoff=0)

        #create menu items in file menu
        self.filemenu.add_command(label='New', command=self.donothing)
        self.filemenu.add_command(label='open', command=self.donothing)
        self.filemenu.add_command(label='save', command=self.donothing)

        #add a horizontal line as seperator
        self.filemenu.add_separator()

        #create another itme below seperator
        self.filemenu.add_command(label='Exit', command=root.destroy)

        #add menu with the name file
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        #crete edit menu
        self.editmenu = Menu(root,tearoff=0)

        #create menu item in edit menu
        self.editmenu.add_command(label='Cut', command=self.donothing)
        self.editmenu.add_command(label='Copy', command=self.donothing)
        self.editmenu.add_command(label='paste', command=self.donothing)

        #add the edit menu with a name edit to the menubar
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)

    def donothing(self):
        pass
root = Tk()

        #title for root window
root.title('A menu example')

        #crete object
obj=mymenudemo(root)

        #definie the size of root window
root.geometry('600x350')

root.mainloop()

from tkinter import*
class mymenudemo:
    def __init__(self, root):
        #create menubar
        self.menubar = Menu(root)

        #attach the menubar to the root window
        root.config(menu=self.menubar)

        #create file menu
        self.filemenu=Menu(root, tearoff=0)

        #create menu items in file menu
        self.filemenu.add_command(label='New', command=self.donothing)
        self.filemenu.add_command(label='open', command=self.openfile)
        self.filemenu.add_command(label='save', command=self.donothing)

        #add a horizontal line as seperator
        self.filemenu.add_separator()

        #create another itme below seperator
        self.filemenu.add_command(label='Exit', command=root.destroy)

        #add menu with the name file
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        #crete edit menu
        self.editmenu = Menu(root,tearoff=0)

        #create menu item in edit menu
        self.editmenu.add_command(label='Cut', command=self.donothing)
        self.editmenu.add_command(label='Copy', command=self.donothing)
        self.editmenu.add_command(label='paste', command=self.donothing)

        #add the edit menu with a name edit to the menubar
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)

    def donothing(self):
        pass

    def openfile(self):
        #open a file dialog box
        self.filename=filedialog.askopenfilename(parent=root, title=
                'select a file', filetypes=(('python files','*.py'),
                            ('all files','*.*'))
        #if cancel button is not clicked

        if (self.filename !=None):
            #open the file
            f=open(self.filename, 'r')
            contents = f.read()
            #create a text box
            self.t=Text(root, width=80,height=20, wrap=WORD)
            self.t.pack()

            self.t.insert(1.0,contents)
            f.close()                                      
root = Tk()

        #title for root window
root.title('A menu example')

        #crete object
obj=mymenudemo(root)

        #definie the size of root window
root.geometry('600x350')

root.mainloop()
'''

