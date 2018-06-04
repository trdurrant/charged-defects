from ipywidgets import widgets
from IPython.display import display, clear_output
from calc_LZ import madelung, lany_zunger, hart2eV

global text_latt, text_sup
text_latt = None
text_eps = None
text_q = None 
text_sup = None

def calc_iic(button):
    print text_latt
    L = float(text_latt.value)*float(text_sup.value)
    epsilon = float(text_eps.value)
    q = float(text_q.value)
    mp = madelung(L, epsilon, q=q)*hart2eV
    lz = lany_zunger(L, epsilon, q=q)*hart2eV
    clear_output()
    display(button)
    print 'L=', L, 'epsilon=', epsilon, 'q=', q
    print 'LZ IIC', lz, 'eV'


def make_button():
    button = widgets.Button(description='Calculate IIC')
    display(button)
         
    button.on_click(calc_iic)

def get_input():
    text_latt = widgets.Text(description='Lattice constant', value='10.0')
    text_eps = widgets.Text(description='Dielectric constant', value='10.0')
    text_q = widgets.Text(description='Charge state', value='1')
    text_sup = widgets.Text(description='Supercell', value='1')
    print text_latt
    display(text_latt)
    display(text_eps)
    display(text_q)
    display(text_sup)


