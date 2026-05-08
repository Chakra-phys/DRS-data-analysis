# This program provides different unique local environment of Li in a DRS cathode material. First, read a vasp poscar file and then decide cut-off distance for neighbours.
# This program was written with a partial help of AI chatbot.
from ase.io import read
from ase.neighborlist import neighbor_list
import numpy as np
from collections import Counter

# Read POSCAR file
atoms = read("str-rand-1978.vasp")
atoms.set_pbc(True)

# Define element groups
TM_elements = {'Ni', 'Mn'}
Li_symbol = 'Li'
O_symbol = 'O'

# Get indices of elements
Li_indices = [i for i, a in enumerate(atoms) if a.symbol == Li_symbol]
TM_indices = [i for i, a in enumerate(atoms) if a.symbol in TM_elements]
O_indices  = [i for i, a in enumerate(atoms) if a.symbol == O_symbol]

# Build neighbor list (cutoff slightly > 2.7 to avoid edge exclusion)
cutoff = 3.2
i_list, j_list, offsets = neighbor_list('ijS', atoms, cutoff=cutoff)

# Collect environment for each O atom
li_env_counts = []

for li_idx in Li_indices:
    o_count = 0
    tm_count = 0
    for i, j, offset in zip(i_list, j_list, offsets):
        if i != li_idx:
            continue
        neighbor_idx = j
        neighbor_symbol = atoms[neighbor_idx].symbol
        vec = atoms.positions[neighbor_idx] + np.dot(offset, atoms.get_cell()) - atoms.positions[li_idx]
        dist = np.linalg.norm(vec)
        if 0.0 < dist < 3.1:
            if neighbor_symbol == 'O':
                o_count += 1
            elif neighbor_symbol in TM_elements:
                tm_count += 1
    li_env_counts.append((o_count, tm_count))

# Count unique (Li, TM) environments
env_counter = Counter(li_env_counts)
total_envs = len(li_env_counts)
unique_envs = len(env_counter)

# Write results
with open("Li_env-Li12-unrlx.dat", "w") as f:
    f.write(f"# Total O atoms: {total_envs}\n")
    f.write(f"# Unique environments: {unique_envs}\n")
    f.write("Li TM Count Frequency\n")
    for (o, tm), count in sorted(env_counter.items()):
        freq = count / total_envs
        f.write(f"{o} {tm} {count} {freq:.4f}\n")

# Optional print summary
print(f"Total O atoms: {total_envs}")
print(f"Unique (Li, TM) environments: {unique_envs}")
print("Results written to 'Li_environments.dat'")
