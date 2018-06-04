import numpy as np


atomic_no, ghosh_radius = np.loadtxt('atomic_radii_ghosh.txt', unpack=True)
atomic_no, element, trash1, trash2 = np.genfromtxt('elements_data.txt', unpack=True, dtype=str)

atomic_no = atomic_no.astype(np.int)

element_no = atomic_no.shape[0]



radius_dict = {}

for i in range(0, element_no):
    radius_dict[element[i]] =  ghosh_radius[i]


def predict_alignment(element, L):

    try:
        atomic_radius = radius_dict[element]

    except KeyError:
        print 'Atomic radius for "{0}" not known'.format(element)
        
        return 0.0


    m = 0.097
    c = 0.045


    atom_delta = m*atomic_radius + c


    vol_fit = 10**3
    vol = L**3
    return (atom_delta*vol_fit)/vol


if __name__ == '__main__':
    print 'Element   Ghosh and Biswas radius'
    print ' (www.mdpi.com/1422-0067/3/2/87/htm) '
    for i in range(0, element_no):
        symbol = element[i]
        print symbol, radius_dict[symbol]
