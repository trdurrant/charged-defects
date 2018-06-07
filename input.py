from ipywidgets import widgets, HBox, Label, Layout
from IPython.display import display, clear_output
from calc_LZ import madelung, lany_zunger, hart2eV
from calc_alignment import predict_alignment

global text_latt

text_latt = widgets.Text(description='', value='10.0')
text_eps = widgets.Text(description='', value='10.0')
text_q = widgets.Text(description='', value='1')
text_sup = widgets.Text(description='', value='1')
    
lab = Layout(width='14%')
    
label_cell = HBox([Label(':: Cell parameters (cubic cell) ::', layout=Layout(width='30%'))])
text_latt_box = HBox([Label('Lattice constant', layout=lab), text_latt, Label('Angstrom')])
text_eps_box  = HBox([Label('Dielectric constant', layout=lab), text_eps, Label('(Relative)')])
text_q_box  = HBox([Label('Defect charge state', layout=lab), text_q, Label('  a. u.', layout=lab)])
text_sup_box  = HBox([Label('Supercell (NxNxN)', layout=lab), text_sup, Label('(Relative)')])

display(label_cell)
display(text_latt_box)
display(text_sup_box)
display(text_eps_box)
display(text_q_box)

label_exchange = HBox([Label(':: Chage in atoms in cell ::', layout=Layout(width='30%'))])
display(label_exchange)

atom_1_type = widgets.Text(value='O', layout=lab)
atom_1_number = widgets.Text(value='-1', layout=lab)
atom_1_box = HBox([Label('Element', layout=lab), atom_1_type, Label('No. added', layout=lab), atom_1_number])

display(atom_1_box)

atom_2_type = widgets.Text(value='H', layout=lab)
atom_2_number = widgets.Text(value='0', layout=lab)
atom_2_box = HBox([Label('Element', layout=lab), atom_2_type, Label('No. added', layout=lab), atom_2_number])

display(atom_2_box)

atom_3_type = widgets.Text(value='He', layout=lab)
atom_3_number = widgets.Text(value='0', layout=lab)
atom_3_box = HBox([Label('Element', layout=lab), atom_3_type, Label('No. added', layout=lab), atom_3_number])

display(atom_3_box)

