from tkinter import*
from tkinter.ttk import *


root = Tk()
root.title('Calculator')
# Calculator icon
root.iconbitmap('calculator.ico')

e = Entry(root, width=49)
e.grid(row=0, column=0, columnspan=4)


def click_button(x):
    '''Displays what you click '''
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(x))

def clear():
    '''This will wipe any previous equations on the calculator and take you back to 0 '''
    e.delete(0,END)

def add():
    '''Addition '''
    one = e.get()
    global a
    global math
    math = 'add'
    a = float(one)
    e.delete(0, END)


def sub():
    ''' Subtraction '''
    one = e.get()
    global a
    global math
    math = 'sub'
    a = float(one)
    e.delete(0, END)

def multi():
    ''' Multiplication '''
    one = e.get()
    global a
    global math
    math = 'multi'
    a = float(one)
    e.delete(0, END)

def div():
    ''' division '''
    one = e.get()
    global a
    global math
    math = 'div'
    a = float(one)
    e.delete(0, END)

def equal():
    b = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, a + float(b))

    if math == 'sub':
        e.insert(0, a - float(b))

    if math == 'multi':
        e.insert(0, round(a * float(b)))

    if math == 'div':
        e.insert(0, int(a / float(b)))



def sqr():
    ''' computes the square of the number currently displayed '''
    one = e.get()
    global a
    a = float(one)
    e.delete(0, END)
    e.insert(0, a**2)



def sqrt():
    ''' square route of a displayed number '''
    one = e.get()
    global a
    a = float(one)
    e.delete(0, END)
    if a < 0:
        e.insert(0, 'Invalid input')
    else:
        e.insert(0, a**0.5)


def cube():
    ''' computes the cube of the displayed number  '''
    one = e.get()
    global a
    a = float(one)
    e.delete(0, END)
    e.insert(0, a**3)

def cubesqrt():
    ''' computes the cube root of the displayed number  '''
    one = e.get()
    global a
    a = float(one)
    e.delete(0, END)
    if a < 0:
        e.insert(0, -(-a)**(1./3.))
    else:
        e.insert(0, a**(1./3.))


def percentage():
    ''' Percentage of a number '''
    one = e.get()
    global b
    b = float(one)/100
    e.insert(0, b)

def bs():
    ''' erases the last number entered '''
    one = e.get()
    global a
    e.delete(0, END)
    a = one[:-1]
    e.insert(0, a)

def multi_inverse():
    ''' we divide 1 by the number '''
    one = float(e.get())
    global a
    a = float(1/one)
    e.insert(0, a)

def ne_po():
    ''' changes the number on screen to a plus or negative '''
    one = e.get()
    a = float(one)
    e.delete(0, END)
    e.insert(0, a*(-1))


# Define Buttons

button_percentage = Button(text='%', command=percentage)
button_cube = Button(text='x³', command=cube )
button_cubesqrt = Button( text='∛', command=cubesqrt )
button_bs = Button(text='⌫', command=bs )


button_multi_inverse = Button(text='¹⁄ₓ', command=multi_inverse)
button_sqr = Button(text='x²', command=sqr )
button_sqrt = Button(text='√', command=sqrt)
button_div = Button(text='÷', command=div)


button_7 = Button(text='7',  command=lambda: click_button(7))
button_8 = Button(text='8', command=lambda: click_button(8))
button_9 = Button(text='9', command=lambda: click_button(9))
button_add = Button(root, text='+', command=add )

button_4 = Button(text='4', command=lambda: click_button(4) )
button_5 = Button(text='5', command=lambda: click_button(5))
button_6 = Button(text='6', command=lambda: click_button(6))
button_sub = Button(text='-', command=sub)

button_1 = Button(text='1', command=lambda: click_button(1) )
button_2 = Button(text='2', command=lambda: click_button(2) )
button_3 = Button(text='3', command=lambda: click_button(3))
button_multi = Button(text='×', command=multi)

button_ne_po = Button(text='±', command=ne_po)
button_0 = Button(text='0', command=lambda: click_button(0))
button_dot = Button(text='.', command=lambda: click_button('.'))
button_equal = Button(text='=', command=equal)


button_clear = Button(text='Clear', command=clear)

# Put the buttons on the screen

button_percentage.grid(row=1, column=0)
button_cube.grid(row=1, column=1)
button_cubesqrt.grid(row=1, column=2)
button_bs.grid(row=1, column=3)


button_multi_inverse.grid(row=2, column=0)
button_sqr.grid(row=2, column=1)
button_sqrt.grid(row=2, column=2)
button_div.grid(row=2, column=3)


button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_multi.grid(row=5, column=3)

button_ne_po.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_dot.grid(row=6, column=2)
button_equal.grid(row=6, column=3)


button_clear.grid(row=7, column=0, columnspan=4)

root.mainloop()
