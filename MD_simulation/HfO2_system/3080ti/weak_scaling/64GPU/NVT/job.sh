#!/bin/sh
#SBATCH -p q123
#SBATCH -J HfO2
#SBATCH -N 16
#SBATCH -o out
#SBATCH --exclusive

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

export CUDA_VISIBLE_DEVICES=0,1,2,3
source /share/public/PWMLFF_test_data/pfsuo/lammps-2billion_nep-close/env.sh
export OMP_NUM_THREADS=1

mpirun -np 64 --bind-to numa --map-by ppr:4:node lmp -k on g 4 -sf kk -pk kokkos -in lmp.in > lmp.out 2>&1

echo "Job $SLURM_JOB_ID done at " `date`
