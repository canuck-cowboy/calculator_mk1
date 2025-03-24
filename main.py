from tkinter import *


def button_append(num):
    global operation

    """
        the following if statement is the final part of this project that fixed the bug, that i was stuck on.
    """
    # if the operation is not an empty string - which is set during Syntax and Arithmetic Errors.
    if operation != '':
        # get the operation from the operation_label, otherwise the operation will just be an empty string
        operation = operation_text.get()

    # cast whatever num is to a string
    num = str(num)

    # append num to the operation
    operation += num
    # set the value of operation_text:textvariable, to what was appended
    operation_text.set(operation)


def clear():
    operation_text.set('')


def equals():
    global operation

    # get the operation from the operation_label
    operation = operation_text.get()
    try:
        result = eval(operation)
        operation_text.set(result)
    # if user divides by 0
    except ZeroDivisionError:
        operation_text.set('Arithmetic Error')
        # since there's an error, we do not want to save 'Arithmetic Error' as our operation, just want to display it
        operation = ''
    # handle syntax errors
    except SyntaxError:
        operation_text.set('Syntax Error')
        # since there's an error, we do not want to save 'Arithmetic Error' as our operation, just want to display it
        operation = ''


# create a tkinter window, with a fixed size and a title
window = Tk()
window.geometry('366x543')
window.resizable(False, False)
window.title('Iron Calculator: Mark I')

# add a window icon to our app
window_icon = PhotoImage(file='calculator.png')
window.iconphoto(True, window_icon)

# ====================================> operation label <===============================================
operation = None  # """global variable used to fix the bug"""
operation_text = StringVar()
operation_label = Label(window,
                        textvariable=operation_text,
                        height=3,
                        width=27,
                        background='white',
                        font=('Ink Free', 16, 'bold'))
operation_label.pack(pady=5)
# ====================================> operation label <===============================================

# add all the buttons
buttons_frame = Frame(window)
buttons_frame.pack()

button_1 = Button(buttons_frame, text='1', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(1))
button_1.grid(row=0, column=0)

button_2 = Button(buttons_frame, text='2', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(2))
button_2.grid(row=0, column=1)

button_3 = Button(buttons_frame, text='3', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(3))
button_3.grid(row=0, column=2)

button_4 = Button(buttons_frame, text='4', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(4))
button_4.grid(row=1, column=0)

button_5 = Button(buttons_frame, text='5', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(5))
button_5.grid(row=1, column=1)

button_6 = Button(buttons_frame, text='6', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(6))
button_6.grid(row=1, column=2)

button_7 = Button(buttons_frame, text='7', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(7))
button_7.grid(row=2, column=0)

button_8 = Button(buttons_frame, text='8', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(8))
button_8.grid(row=2, column=1)

button_9 = Button(buttons_frame, text='9', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(9))
button_9.grid(row=2, column=2)

# idle button with its image: for future projects
keyboard_image = PhotoImage(file='keyboard.png')
button_idle = Button(buttons_frame, image=keyboard_image, state=DISABLED, width=85, height=80, relief=FLAT)
button_idle.grid(row=3, column=0)

button_0 = Button(buttons_frame, text='0', width=9, height=4, font=35, relief=GROOVE, command=lambda: button_append(0))
button_0.grid(row=3, column=1)

button_dot = Button(buttons_frame, text='.', width=9, height=4, font=35, relief=GROOVE,
                    command=lambda: button_append('.'))
button_dot.grid(row=3, column=2)

button_divide = Button(buttons_frame, text='/', width=9, height=4, font=35, relief=GROOVE,
                       command=lambda: button_append('/'))
button_divide.grid(row=0, column=3)

button_multiply = Button(buttons_frame, text='*', width=9, height=4, font=35, relief=GROOVE,
                         command=lambda: button_append('*'))
button_multiply.grid(row=1, column=3)

button_subtract = Button(buttons_frame, text='-', width=9, height=4, font=35, relief=GROOVE,
                         command=lambda: button_append('-'))
button_subtract.grid(row=2, column=3)

button_add = Button(buttons_frame, text='+', width=9, height=4, font=35, relief=GROOVE,
                    command=lambda: button_append('+'))
button_add.grid(row=3, column=3)

# bottom part
bottom_frame = Frame(window)
bottom_frame.pack(pady=10)

button_clear = Button(bottom_frame, text='clear', width=17, height=4, font=35, relief=RAISED, command=clear)
button_clear.grid(row=0, column=1, padx=7)

button_equal = Button(bottom_frame, text='=', width=17, height=4, font=35, relief=RAISED, command=equals)
button_equal.grid(row=0, column=2, padx=7)

# enable KeyPresses too
window.bind('<KeyPress-0>', lambda event: button_append(0))
window.bind('<KeyPress-1>', lambda event: button_append(1))
window.bind('<KeyPress-2>', lambda event: button_append(2))
window.bind('<KeyPress-3>', lambda event: button_append(3))
window.bind('<KeyPress-4>', lambda event: button_append(4))
window.bind('<KeyPress-5>', lambda event: button_append(5))
window.bind('<KeyPress-6>', lambda event: button_append(6))
window.bind('<KeyPress-7>', lambda event: button_append(7))
window.bind('<KeyPress-8>', lambda event: button_append(8))
window.bind('<KeyPress-9>', lambda event: button_append(9))
window.bind('<KeyPress-.>', lambda event: button_append('.'))
window.bind('<KeyPress-slash>', lambda event: button_append('/'))
window.bind('<KeyPress-asterisk>', lambda event: button_append('*'))
window.bind('<KeyPress-minus>', lambda event: button_append('-'))
window.bind('<KeyPress-plus>', lambda event: button_append('+'))
window.bind('<Return>', lambda event: equals())
window.bind('<BackSpace>', lambda event: clear())
window.bind('<Escape>', lambda event: quit())

# run the tkinter app
window.mainloop()
