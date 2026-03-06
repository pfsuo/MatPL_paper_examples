#!/bin/sh
#SBATCH -p q123
#SBATCH -J HfO2
#SBATCH -N 1
#SBATCH -o out
#SBATCH --gres=gpu:1
#SBATCH -w gn135

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

source /share/public/PWMLFF_test_data/pfsuo/lammps-2billion_nep-close/env.sh
export OMP_NUM_THREADS=1

mpirun -np 1 --bind-to numa --map-by ppr:1:node lmp -k on g 1 -sf kk -pk kokkos -in lmp.in > lmp.out 2>&1

echo "Job $SLURM_JOB_ID done at " `date`
