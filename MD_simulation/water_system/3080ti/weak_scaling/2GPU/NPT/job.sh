#!/bin/sh
#SBATCH -p q123
#SBATCH -J water
#SBATCH -N 1
#SBATCH -o out
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:2
#SBATCH --gpus-per-task=1
#SBATCH -w gn134

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

source /share/public/PWMLFF_test_data/pfsuo/lammps-2billion_nep-close/env.sh
export OMP_NUM_THREADS=1

mpirun -np 2 --bind-to numa --map-by ppr:2:node lmp -k on g 2 -sf kk -pk kokkos -in lmp.in > lmp.out 2>&1

echo "Job $SLURM_JOB_ID done at " `date`
