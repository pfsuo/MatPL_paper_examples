#!/bin/bash
rm -rf {1..23}
for i in {1..23};do
j=$((i+1))
mkdir ${i} && cd ${i}
cat > lmp.in << EOF
variable        NSTEPS          equal 10000
variable        THERMO_FREQ     equal 100
variable        DUMP_FREQ       equal 10
variable        restart         equal 0
variable        TEMP            equal 300.000000
variable        PRESS           equal 0.000000
variable        TAU_T           equal 0.050000
variable        TAU_P           equal 0.500000

package kokkos neigh half comm device
newton on

units           metal
boundary        p p p
atom_style      atomic

neighbor        1.0 bin
neigh_modify    delay 10

#box              tilt large
if "\${restart} > 0" then "read_restart lmps.restart.*" else "read_data ../../../216_water/conf.lmp"
#change_box       all triclinic
replicate   $i $(($i*2)) $(($i*2))

mass   1    15.999
mass   2    1.00784
pair_style   matpl/nep/kk /data/home/pfsuo/pfsuo/software/build/nep-data/2023_Xu_liquid_water/nep.txt
pair_coeff       * * O H

thermo_style    custom step temp pe ke etotal press vol
thermo          \${THERMO_FREQ}

if "\${restart} == 0" then "velocity        all create \${TEMP} 35826"
fix             1 all nvt/kk temp \${TEMP} \${TEMP} \${TAU_T} #iso \${PRESS} \${PRESS} \${TAU_P}

timestep        0.000500
run             \${NSTEPS} upto
EOF
cat > job.sh << EOF
#!/bin/sh
#SBATCH -p 4090
#SBATCH -J water
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:4
#SBATCH --gpus-per-task=1
#SBATCH -o out
#SBATCH -w gn202

echo "Starting job \$SLURM_JOB_ID at " \`date\`
echo "SLURM_SUBMIT_DIR is \$SLURM_SUBMIT_DIR"
echo "Running on nodes: \$SLURM_NODELIST"

source /share/public/PWMLFF_test_data/pfsuo/lammps-2billion_nep-close/env.sh
export OMP_NUM_THREADS=1

mpirun -np \$SLURM_NPROCS --bind-to numa --map-by ppr:\$SLURM_NPROCS:node lmp -k on g \$SLURM_NPROCS -sf kk -pk kokkos -in lmp.in > lmp.out 2>&1
cd ../${j} && sbatch job.sh

echo "Job \$SLURM_JOB_ID done at " \`date\`
EOF
if [ $i -eq 1 ]; then
sbatch job.sh
fi
cd ..
done
