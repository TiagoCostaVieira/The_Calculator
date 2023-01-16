
from tkinter import *
from tkinter import ttk


def the_numbers_for_the_list(number):
    number = number['text']
    if number == 'x':
        calculation.append('*')
        calculation_lb['text'] = calculation
    elif number == '÷':
        calculation.append('/')
        calculation_lb['text'] = calculation
    else:
        calculation.append(number)
        calculation_lb['text'] = calculation



def calculate():
    global calculation
    try:
        calculation_lb['text'] = eval(str("".join(calculation)))
        calculation = []
    except:
        calculation_lb['text'] = 'E R R O'
        calculation = []
def clear():
    global conta
    calculation_lb['text'] = ' '
    calculation = []

tela = Tk()
tela.title('Calculadora')
tela.geometry('350x500')
tela.resizable(True, False)
calculation = []


calculation_lb = Label(tela, text = '', font = 12)
calculation_lb.pack(side = TOP, anchor = E)

number_one = Button (tela, text = '1', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_one))
number_one.place(x = 10, y = 100)

number_two = Button (tela, text = '2', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_two))
number_two.place(x = 90, y = 100)

number_three = Button (tela, text = '3', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_three))
number_three.place(x = 170, y = 100)

number_four = Button (tela, text = '4', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_four))
number_four.place(x = 10, y = 180)

number_five = Button (tela, text = '5', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_five))
number_five.place(x = 90, y = 180 )

number_six = Button (tela, text = '6', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_six))
number_six.place(x = 170, y = 180)

number_seven = Button (tela, text = '7', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_seven))
number_seven.place(x = 10, y = 260)

number_eight = Button (tela, text = '8', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_eight))
number_eight.place(x = 90, y = 260)

number_nine = Button (tela, text = '9', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_nine))
number_nine.place(x = 170, y = 260)

number_zero = Button (tela, text = '0', width = 8, height = 4, command = lambda : the_numbers_for_the_list(number_zero))
number_zero.place(x = 10, y = 340)

dot = Button(tela, text = '.', width = 8, height = 4, command = lambda : the_numbers_for_the_list(dot))
dot.place(x = 170, y = 340)

result = Button (tela, text = '=', width = 20, height = 4, fg = 'white', bg = 'red', command = calculate)
result.place(x = 170,y = 420)

delete = Button (tela, text = 'C', width = 8, height = 4, fg = "white", bg = "black", command = clear)
delete.place(x = 90, y = 340)

plus = Button(tela, text = '+', width = 8, height = 4, command = lambda : the_numbers_for_the_list(plus))
plus.place(x = 260, y = 100)

subtraction = Button(tela, text = '-', width = 8, height = 4, command = lambda : the_numbers_for_the_list(subtraction))
subtraction.place(x = 260, y = 180)

multiply = Button(tela, text = 'x', width = 8, height = 4, command = lambda : the_numbers_for_the_list(multiply))
multiply.place(x = 260, y = 260)

division = Button(tela, text = '÷', width = 8, height = 4, command = lambda : the_numbers_for_the_list(division))
division.place(x = 260, y = 340)

right_parenthesis = Button(tela, text = '(', width = 8, height = 4, command = lambda : the_numbers_for_the_list(right_parenthesis))
right_parenthesis.place(x = 10, y = 420)

left_parenthesis = Button(tela, text = ')', width = 8, height = 4, command = lambda : the_numbers_for_the_list(left_parenthesis))
left_parenthesis.place(x = 90, y = 420)


tela.mainloop()
