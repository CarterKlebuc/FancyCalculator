from sympy import *
import matplotlib as m
import matplotlib.pyplot as mpl
from numpy import linspace
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import calculations as cal
from PySimpleGUI import *

# GUI Layout
layout = [
    [Text('', size=(10, 1), text_color='white', key='mode_id')],
    [
        Text('',
             size=(15, 1),
             font=('Helvetica', 18),
             text_color='white',
             key='input')
    ],
    #[Combo(['Hello'])],
    [Canvas(key = '-CANVAS-')],
    [Text('' * 10)],
    [
        ReadFormButton('c'),
        ReadFormButton('x'),
        ReadFormButton('∫'),
        ReadFormButton('∫ab'),
        ReadFormButton('d/dx')
    ],
    [
        ReadFormButton('7'),
        ReadFormButton('8'),
        ReadFormButton('9'),
        ReadFormButton('/'),
        ReadFormButton('(')
    ],
    [
        ReadFormButton('4'),
        ReadFormButton('5'),
        ReadFormButton('6'),
        ReadFormButton('*'),
        ReadFormButton(')')
    ],
    [
        ReadFormButton('1'),
        ReadFormButton('2'),
        ReadFormButton('3'),
        ReadFormButton('-'),
        ReadFormButton('graph')
    ],
    [
        ReadFormButton('.'),
        ReadFormButton('0'),
        ReadFormButton('='),
        ReadFormButton('+'),
        ReadFormButton('**')
    ],
]

form = FlexForm('CALCULATOR',
                default_button_element_size=(5, 2),
                auto_size_buttons=False,
                grab_anywhere=False,
                resizable=True)
form.Layout(layout)

Result = ''
mode = 'normal'
graph_present = False

m.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Program Loop
while True:
  # Button Values
  x = Symbol('x')
  button, value = form.Read()

  if button == 'c':
    Result = ''
    form.find_element('input').Update(Result)
    form.find_element('-CANVAS-').delete("all")
    graph_present = False

  elif button == '=':
    if mode == 'normal':
      Answer = eval(Result)
      Answer = str(round(float(Answer), 3))
      form.find_element('input').Update(Answer)
      Result = Answer

    elif mode == 'indefinite_int':
      Answer = cal.in_integral_calc(Result)
      form.find_element('input').Update(Answer)
      Result = Answer

    elif mode == 'definite_int':
      form.find_element('input').Update('')
      form.find_element('mode_id').Update('Enter Upper Bound')
      button, value = form.Read()
      upper_bound = int(button)
      form.find_element('input').Update('')
      form.find_element('mode_id').Update('Enter Lower Bound')
      button, value = form.Read()
      lower_bound = int(button)
      Answer = cal.def_integral_calc(Result, upper_bound, lower_bound)
      form.find_element('input').Update(Answer)
      Result = Answer
      form.find_element('mode_id').Update('')

    elif mode == 'derivative':
      Answer = cal.derivative_calc(Result)
      form.find_element('input').Update(Answer)
      Result = Answer

    elif mode == 'graph':
      fig = m.figure.Figure(figsize=(5, 4), dpi=100)
      x_vals = linspace(0, 10, 100)
      lam_x = lambdify(x, Result, modules=['numpy'])
      y_vals = lam_x(x_vals)
      fig.add_subplot(111).plot(x_vals, y_vals)
      fig_canvas_agg = draw_figure(form["-CANVAS-"].TKCanvas, fig)
      #mpl.show()

  elif button == 'd/dx':
    mode = 'derivative'
    form.find_element('mode_id').Update('Derivative')
    Result = ''
    form.find_element('input').Update(Result)

  elif button == '∫':
    mode = 'indefinite_int'
    form.find_element('mode_id').Update('Indefinite Integral')
    Result = ''
    form.find_element('input').Update(Result)

  elif button == '∫ab':
    mode = 'definite_int'
    form.find_element('mode_id').Update('Definite Integral')
    Result = ''
    form.find_element('input').Update(Result)

  elif button == 'graph':
    mode = 'graph'
    form.find_element('mode_id').Update('Graph')
    Result = ''
    form.find_element('input').Update(Result)
    graph_present = True

  elif button == 'Quit' or button == None:
    break

  else:
    Result += button
    form.find_element('input').Update(Result)