import numpy as np
import matplotlib.pyplot as plt
import os, subprocess

size = 20
str2float = {'Matom-step/s':1e6, 'katom-step/s':1e3}
MatPL_Natoms = [int(subprocess.getoutput("awk '/atoms/ {print $1}' ../MatPL/%d/*out | tail -2 | head -1"%(i))) for i in range(1,22)]
MatPL_Speeds = [float(subprocess.getoutput("awk '/Perf/ {print $8}' ../MatPL/%d/*out "%(i)))*str2float[subprocess.getoutput("awk '/Perf/ {print $NF}' ../MatPL/nep-close/%dx%dx%d/*out "%(i,i,i))] for i in range(1,22)]
GPUMD_49_Natoms = [int(subprocess.getoutput("awk '/Number/ {print $NF}' ../GPUMD/v4.9/%dx%dx%d/*out | tail -1"%(i,i,i))[:-1]) for i in range(1,19)]
GPUMD_49_Speeds = [float(subprocess.getoutput("awk '/Speed/ {print $6}' ../GPUMD/v4.9/%dx%dx%d/*out | tail -1"%(i,i,i))) for i in range(1,19)]
DP_Natoms = [int(subprocess.getoutput("awk '/atoms/ {print $1}' ../DP/%dx%dx%d/*out | tail -2 | head -1"%(i,i,i))) for i in range(1,6)]
DP_Speeds = [float(subprocess.getoutput("awk '/Perf/ {print $8}' ../DP/%dx%dx%d/*out "%(i,i,i)))*str2float[subprocess.getoutput("awk '/Perf/ {print $NF}' ../DP/%dx%dx%d/*out "%(i,i,i))] for i in range(1,6)]
MACE_Natoms = [648, 648*2, 648*4, 648*8]
MACE_Speeds = [float(subprocess.getoutput("awk '/Speed is/ {print $3}' ../MACE/%s/out | tail -1"%(i))) for i in ['1x1x1','1x1x2','1x2x2','2x2x2']]
eqV2_Natoms = [480]
eqV2_Speeds = [2.569612E+03]
eSEN_Natoms = [330]
eSEN_Speeds = [6.567206E+02]

plt.plot(MatPL_Natoms, MatPL_Speeds, 'o:',lw=3,label='MatPL-2026.3',alpha=.7)
plt.plot(GPUMD_49_Natoms, GPUMD_49_Speeds, 'o-',lw=3,label='GPUMD-v4.9',alpha=.7)
plt.plot(DP_Natoms, DP_Speeds, 'o-',lw=3,label='DP',alpha=.7)
plt.plot(MACE_Natoms, MACE_Speeds, 'o-',lw=3,label='MACE-medium',alpha=.7)
plt.plot(eqV2_Natoms, eqV2_Speeds, 'o-',lw=3,label='eqV2_31M',alpha=.7)
plt.plot(eSEN_Natoms, eSEN_Speeds, 'o-',lw=3,label='eSEN_30M',alpha=.7)
plt.xscale('log')
plt.yscale('log')
plt.xticks(size=size-2,fontweight='bold')
plt.yticks(size=size-2,fontweight='bold')
plt.xlabel('Number of atoms',size=size+2,fontweight='bold')
plt.ylabel('Speed (atom-step/s)',size=size+2,fontweight='bold')
plt.legend(prop={'weight':'bold','size':size-6.5})
bwith = 2
TK = plt.gca()
TK.spines['bottom'].set_linewidth(bwith)
TK.spines['left'].set_linewidth(bwith)
TK.spines['top'].set_linewidth(bwith)
TK.spines['right'].set_linewidth(bwith)
plt.tight_layout()
plt.savefig('Speed_v4.9.png',dpi=600)
plt.savefig('Speed_v4.9.svg')
plt.close()

print('MatPL_Natoms')
print(MatPL_Natoms)
print('MatPL_Speeds')
print(MatPL_Speeds)
print('GPUMD_49_Natoms')
print(GPUMD_49_Natoms)
print('GPUMD_49_Speeds')
print(GPUMD_49_Speeds)
print('DP_Natoms')
print(DP_Natoms)
print('DP_Speeds')
print(DP_Speeds)
print('MACE_Natoms')
print(MACE_Natoms)
print('MACE_Speeds')
print(MACE_Speeds)
print('eqV2_Natoms')
print(eqV2_Natoms)
print('eqV2_Speeds')
print(eqV2_Speeds)
print('eSEN_Natoms')
print(eSEN_Natoms)
print('eSEN_Speeds')
print(eSEN_Speeds)
