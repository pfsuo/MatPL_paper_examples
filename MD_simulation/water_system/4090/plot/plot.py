import numpy as np
import matplotlib.pyplot as plt
import os, subprocess

size = 20
str2float = {'Matom-step/s':1e6, 'katom-step/s':1e3}
MatPL_1GPU_Natoms = [int(subprocess.getoutput("awk '/atoms/ {print $1}' ../1GPU/MatPL/%d/*out | tail -2 | head -1"%(i))) for i in range(1,22)]
MatPL_1GPU_Speeds = [float(subprocess.getoutput("awk '/Perf/ {print $8}' ../1GPU/MatPL/%d/*out "%(i)))*str2float[subprocess.getoutput("awk '/Perf/ {print $NF}' ../1GPU/MatPL/%d/*out "%(i))] for i in range(1,22)]
MatPL_2GPU_Natoms = [int(subprocess.getoutput("awk '/atoms/ {print $1}' ../2GPU/MatPL/%d/*out | tail -2 | head -1"%(i))) for i in range(1,21)]
MatPL_2GPU_Speeds = [float(subprocess.getoutput("awk '/Perf/ {print $8}' ../2GPU/MatPL/%d/*out "%(i)))*str2float[subprocess.getoutput("awk '/Perf/ {print $NF}' ../2GPU/MatPL/%d/*out "%(i))] for i in range(1,21)]
MatPL_4GPU_Natoms = [int(subprocess.getoutput("awk '/atoms/ {print $1}' ../4GPU/MatPL/%d/*out | tail -2 | head -1"%(i))) for i in range(1,21)]
MatPL_4GPU_Speeds = [float(subprocess.getoutput("awk '/Perf/ {print $8}' ../4GPU/MatPL/%d/*out "%(i)))*str2float[subprocess.getoutput("awk '/Perf/ {print $NF}' ../4GPU/MatPL/%d/*out "%(i))] for i in range(1,21)]
GPUMD_1GPU_Natoms = [int(subprocess.getoutput("awk '/Number/ {print $NF}' ../1GPU/GPUMD/v4.9/%dx%dx%d/*out | tail -1"%(i,i,i))[:-1]) for i in range(1,19)]
GPUMD_1GPU_Speeds = [float(subprocess.getoutput("awk '/Speed/ {print $6}' ../1GPU/GPUMD/v4.9/%dx%dx%d/*out | tail -1"%(i,i,i))) for i in range(1,19)]
GPUMD_2GPU_Natoms = [int(subprocess.getoutput("awk '/Number/ {print $NF}' ../2GPU/GPUMD/%d/*out | tail -1"%(i))[:-1]) for i in range(2,19)]
GPUMD_2GPU_Speeds = [float(subprocess.getoutput("awk '/Speed/ {print $6}' ../2GPU/GPUMD/%d/*out | tail -1"%(i))) for i in range(2,19)]
GPUMD_4GPU_Natoms = [int(subprocess.getoutput("awk '/Number/ {print $NF}' ../4GPU/GPUMD/%d/*out | tail -1"%(i))[:-1]) for i in range(4,19)]
GPUMD_4GPU_Speeds = [float(subprocess.getoutput("awk '/Speed/ {print $6}' ../4GPU/GPUMD/%d/*out | tail -1"%(i))) for i in range(4,19)]

plt.plot(MatPL_4GPU_Natoms, MatPL_4GPU_Speeds, 'o-',c='C0',lw=3,label='MatPL_4x4090',alpha=.7)
plt.plot(MatPL_2GPU_Natoms, MatPL_2GPU_Speeds, 's--',c='C0',lw=3,label='MatPL_2x4090',alpha=.7)
plt.plot(MatPL_1GPU_Natoms, MatPL_1GPU_Speeds, '^:',c='C0',lw=3,label='MatPL_1x4090',alpha=.7)
plt.plot(GPUMD_4GPU_Natoms, GPUMD_4GPU_Speeds, 'o-',c='C1',lw=3,label='GPUMD_4x4090',alpha=.7)
plt.plot(GPUMD_2GPU_Natoms, GPUMD_2GPU_Speeds, 's--',c='C1',lw=3,label='GPUMD_2x4090',alpha=.7)
plt.plot(GPUMD_1GPU_Natoms, GPUMD_1GPU_Speeds, '^:',c='C1',lw=3,label='GPUMD_1x4090',alpha=.7)
plt.xscale('log')
plt.yscale('log')
plt.xticks(size=size-2,fontweight='bold')
plt.yticks(size=size-2,fontweight='bold')
plt.xlabel('Number of atoms',size=size+2,fontweight='bold')
plt.ylabel('Speed (atom-step/s)',size=size+2,fontweight='bold')
plt.legend(prop={'weight':'bold','size':size-4.5})
bwith = 2
TK = plt.gca()
TK.spines['bottom'].set_linewidth(bwith)
TK.spines['left'].set_linewidth(bwith)
TK.spines['top'].set_linewidth(bwith)
TK.spines['right'].set_linewidth(bwith)
plt.tight_layout()
plt.savefig('Speed_MatPL_vs_GPUMD.png',dpi=600)
plt.savefig('Speed_MatPL_vs_GPUMD.svg')
plt.close()

print('MatPL_1GPU_Natoms')
print(MatPL_1GPU_Natoms)
print('MatPL_1GPU_Speeds')
print(MatPL_1GPU_Speeds)
print('MatPL_2GPU_Natoms')
print(MatPL_2GPU_Natoms)
print('MatPL_2GPU_Speeds')
print(MatPL_2GPU_Speeds)
print('MatPL_4GPU_Natoms')
print(MatPL_4GPU_Natoms)
print('MatPL_4GPU_Speeds')
print(MatPL_4GPU_Speeds)
print('GPUMD_1GPU_Natoms')
print(GPUMD_1GPU_Natoms)
print('GPUMD_1GPU_Speeds')
print(GPUMD_1GPU_Speeds)
print('GPUMD_2GPU_Natoms')
print(GPUMD_2GPU_Natoms)
print('GPUMD_2GPU_Speeds')
print(GPUMD_2GPU_Speeds)
print('GPUMD_4GPU_Natoms')
print(GPUMD_4GPU_Natoms)
print('GPUMD_4GPU_Speeds')
print(GPUMD_4GPU_Speeds)
