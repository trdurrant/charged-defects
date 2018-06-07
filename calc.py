from ipywidgets import widgets, HBox, Label, Layout
from IPython.display import display, clear_output
from calc_LZ import madelung, lany_zunger, hart2eV
from calc_alignment import predict_alignment

button = widgets.Button(description='Calculate Corrections')
display(button)

def calc_iic(button):
    print text_latt
    L = float(text_latt.value)*float(text_sup.value)
    epsilon = float(text_eps.value)
    q = float(text_q.value)
    mp = madelung(L, epsilon, q=q)*hart2eV
    lz = lany_zunger(L, epsilon, q=q)*hart2eV
    clear_output()
    display(button)
    print 'Image interaction correction'
    print 'L =', L, '(Angstrom) ' 'epsilon=', epsilon, 'q =', q
    print 'LZ IIC', lz, 'eV'
    print '\n'
    
    N_1 = int(atom_1_number.value)
    element_1 = str(atom_1_type.value)
    alignment_1 = predict_alignment(element_1, L)

    N_2 = int(atom_2_number.value)
    element_2 = str(atom_2_type.value)
    alignment_2 = predict_alignment(element_2, L)

    N_3 = int(atom_3_number.value)
    element_3 = str(atom_3_type.value)
    alignment_3 = predict_alignment(element_3, L)

    
    print 'Prediction of potential alignment'
    print 'Correction for {0}'.format(element_1), alignment_1*q*N_1, 'eV'
    print 'Correction for {0}'.format(element_2), alignment_2*q*N_2, 'eV'
    print 'Correction for {0}'.format(element_3), alignment_3*q*N_3, 'eV'
    print 'q =', q, '(Electron charges)', 'L =', L, '(Angstrom)'


    
    print '\n'
    print 'Image Interaction correction (LZ) =', lz, 'eV'
    print 'Predicted alignment correction    =', q*(alignment_1*N_1 + alignment_2*N_2 + alignment_3*N_3), 'eV'
    print 'Combined correction               =', lz + q*(alignment_1*N_1 + alignment_2*N_2 + alignment_3*N_3), 'eV'

         
button.on_click(calc_iic)
