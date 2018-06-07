import numpy as np

# Define global constants
hart2eV = 27.21138505 # 2010 CODATA recomended values
bohr = 5.2917721092e-11

# Unit conversion factors
ang2Bohr = 1e-10/bohr
bohr2Ang = 1.0/ang2Bohr

c_sh = 0.369

def madelung(L, epsilon, q=1): 
    """ Get the defect interaction energy of a single point charge """
    # Convert inputf from Bohr to Ang
    L = L*ang2Bohr
    pointEng = (2.8373*(q**2))/(2.0*L) 
    return pointEng/epsilon

def lany_zunger(L, epsilon, q=1):

    mp = madelung(L, epsilon, q=q)

    f = 1.0 - c_sh*(1.0-(epsilon**-1))

    return f*mp


if __name__ == '__main__':
    # 3x3x3
    #L = 12.5399925*ang2Bohr
    # 4x4x4
    #L = 16.719990*ang2Bohr
    # 5x5x5
    L = 20.8999875*ang2Bohr
    
    epsilon = 2.59874080933
    #epsilon = 3.1
    #epsilon = 2.66553602976
    #epsilon = 8.03134051458
    print 'q=1 ::'
    print 'MP', madelung(L, epsilon)*hart2eV, 'eV'
    print 'LZ', lany_zunger(L, epsilon)*hart2eV, 'eV'
            
    print 'q=2 ::'
    print 'MP', madelung(L, epsilon, q=2)*hart2eV, 'eV'
    print 'LZ', lany_zunger(L, epsilon, q=2)*hart2eV, 'eV'





