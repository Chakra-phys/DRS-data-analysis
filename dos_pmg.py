# This is program to plot total and partial density of states (DOS)
from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp.outputs import Vasprun
#%matplotlib inline
import matplotlib.pyplot as plt


# load data
result = Vasprun('./fix_U/vasprun.xml', parse_potcar_file=False)
structure = result.structures

complete_dos = result.complete_dos
plotter = DosPlotter()

  
pdos_Ni1=complete_dos.get_element_spd_dos('Ni')

pdos_Mn = complete_dos.get_element_spd_dos('Mn')
pdos_O = complete_dos.get_element_spd_dos('O')
#pdos_O46=complete_dos.get_site_spd_dos(structure[0][45])


#plotter = DosPlotter()
plotter.add_dos('Total DOS', result.tdos)
plotter.add_dos('Ni(d)', pdos_Ni1[OrbitalType.d])
plotter.add_dos('Mn(d)', pdos_Mn[OrbitalType.d])
plotter.add_dos('O(p)', pdos_O[OrbitalType.p])

plotter.get_plot(xlim=(-6, 6), ylim=(-50, 50))
plt.savefig('LNMO_dos.tif', dpi=500)
