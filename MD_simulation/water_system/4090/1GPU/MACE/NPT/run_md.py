from ase.io import read
from ase.build import bulk, make_supercell, surface
from ase.units import fs
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from mace.calculators import mace_mp
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.npt import NPT
from ase.optimize import LBFGS
from ase.constraints import FixAtoms
import numpy as np
import time

T = 300
P = 1.01325
P_in_ev_per_ang3 = P / 1602176.6208
atoms = read("../../../216_water/model.xyz")
pos = atoms.get_scaled_positions()
atoms.cell *= 1.05
atoms.set_scaled_positions(pos)
atoms = make_supercell(atoms,[[2,0,0],[0,2,0],[0,0,1]])
n_atoms = len(atoms)
if not NPT._isuppertriangular(atoms.get_cell()):
    a, b, c, alpha, beta, gamma = atoms.cell.cellpar()
    angles = np.radians((alpha, beta, gamma))
    sin_a, sin_b, _sin_g = np.sin(angles)
    cos_a, cos_b, cos_g = np.cos(angles)
    cos_p = (cos_g - cos_a * cos_b) / (sin_a * sin_b)
    cos_p = np.clip(cos_p, -1, 1)
    sin_p = (1 - cos_p**2) ** 0.5
    new_basis = [
        (a * sin_b * sin_p, a * sin_b * cos_p, a * cos_b),
        (0, b * sin_a, b * cos_a),
        (0, 0, c),
    ]
    atoms.set_cell(new_basis, scale_atoms=True)

calc = mace_mp(model="medium")
atoms.calc = calc
#opt = LBFGS(atoms)
#opt.run(fmax=0.05)

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
#indices = [atom.index for atom in atoms if atom.position[2] < 18.0]
#indices += [atom.index for atom in atoms if atom.position[2] > 54.5]
#v = atoms.get_velocities()
#for i in indices:
#    v[i] = 0.
#atoms.set_velocities(v)
#c = FixAtoms(indices=indices)
#atoms.set_constraint(c)

#print("Beginning Berendsen equilibration")
#dyn_nvt = NVTBerendsen(
#atoms,
#trajectory=None,
#timestep=1.*fs,
#temperature_K=T,
#taut=1.*100*fs,
#logfile="Berendsen.log",
#loginterval=10
#)
#dyn_nvt.run(20000)

print("Beginning Nose-Hoover NPT equilibration")
dyn_npt = NPT(
atoms=atoms,
timestep=.5*fs,
temperature_K=T,
externalstress=P_in_ev_per_ang3,
ttime=50*fs,
pfactor=50*fs,
trajectory="nose_hoover.traj",
logfile="nose_hoover.log",
loginterval=100
)
begin = time.time()
dyn_npt.run(10000)
end = time.time()
print("Speed is %E5 atoms-step/s"%(1E4*n_atoms/(end-begin)))
