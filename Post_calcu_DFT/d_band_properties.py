import warnings
warnings.filterwarnings('ignore')
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.core import Spin
from collections import namedtuple
from ase.dft import get_distribution_moment
import numpy as np
from ase.io import read

# ---------- USER INPUT ----------
vasprun = "vasprun.xml"
poscar = "POSCAR"
mode = "all"      # choose from: "all", "sur", or atom index (int)
spin_channel = "up"   # "up" or "down"
output = "band_centre_width_filling.dat"
# --------------------------------

# --- Read vasprun.xml ---
dosrun = Vasprun(vasprun)
dos = dosrun.complete_dos
energies = dosrun.tdos.energies - dosrun.efermi  # align to EF=0

# --- Read POSCAR for atom names/counts ---
lines = open(poscar).read().splitlines()
atoms = lines[5].split()
atoms_number = list(map(int, lines[6].split()))

# --- Build ASE structure for z-coordinates (if needed) ---
structure = read(poscar)

# --- Determine which atoms to analyze ---
if mode == "sur":
    z_coords = [round(site.position[2], 3) for site in structure]
    max_z = max(z_coords)
    sites = [i for i, z in enumerate(z_coords) if z >= max_z - 1.0]
elif mode == "all":
    sites = list(range(len(structure)))
else:
    sites = [int(mode)]

# --- Open output file ---
with open(output, 'w') as f:
    header = ("#Atom   s_center  s_width  p_center  p_width  "
              "d_center  d_width  f_center  f_width  d_filling  frac_fill\n")
    f.write(header)

    for site in sites:
        site_dos = dos.get_site_spd_dos(dos.structure[site])
        site_named = namedtuple('Struct', site_dos.keys())(*site_dos.values())
        el = structure[site].symbol

        # --- Get orbital-projected DOS based on block type ---
        if spin_channel == "up":
            site_s = site_named.s.densities[Spin.up]
            site_p = site_named.p.densities.get(Spin.up, np.zeros_like(energies))
            site_d = site_named.d.densities.get(Spin.up, np.zeros_like(energies))
            site_f = site_named.f.densities.get(Spin.up, np.zeros_like(energies)) \
                     if hasattr(site_named, 'f') else np.zeros_like(energies)
        else:
            site_s = site_named.s.densities[Spin.down]
            site_p = site_named.p.densities.get(Spin.down, np.zeros_like(energies))
            site_d = site_named.d.densities.get(Spin.down, np.zeros_like(energies))
            site_f = site_named.f.densities.get(Spin.down, np.zeros_like(energies)) \
                     if hasattr(site_named, 'f') else np.zeros_like(energies)

        # --- Compute energy spacing for integration ---
        dE = np.mean(np.diff(energies))

        # --- Compute moments (center and width) ---
        s_center = get_distribution_moment(energies, site_s, order=1)
        s_width = np.sqrt(get_distribution_moment(energies, site_s, order=2))
        p_center = get_distribution_moment(energies, site_p, order=1)
        p_width = np.sqrt(get_distribution_moment(energies, site_p, order=2))
        d_center = get_distribution_moment(energies, site_d, order=1)
        d_width = np.sqrt(get_distribution_moment(energies, site_d, order=2))
        f_center = get_distribution_moment(energies, site_f, order=1)
        f_width = np.sqrt(get_distribution_moment(energies, site_f, order=2))

        # --- Compute d-band filling ---
        total_fill = np.sum(site_d) * dE  # total number of d-electrons
        occ_mask = energies <= 0          # below Fermi
        filled = np.sum(site_d[occ_mask]) * dE
        frac_fill = filled / total_fill if total_fill > 1e-8 else np.nan

        # --- Find atomic index relative to species ---
        n = atoms.index(el)
        z = sum(atoms_number[:n])
        atom_label = f"{el}-{site + 1 - z}"

        f.write(f"{atom_label:8s} {s_center:8.3f} {s_width:8.3f} "
                f"{p_center:8.3f} {p_width:8.3f} {d_center:8.3f} {d_width:8.3f} "
                f"{f_center:8.3f} {f_width:8.3f} {total_fill:10.3f} {frac_fill:10.3f}\n")

print(f"✅ Results written to: {output}")

