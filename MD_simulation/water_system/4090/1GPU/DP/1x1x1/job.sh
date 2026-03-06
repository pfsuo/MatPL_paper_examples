#!/bin/sh
#SBATCH -p 4090
#SBATCH -J water
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --gpus-per-task=1
#SBATCH -o out
#SBATCH -w gn202

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

module purge
export OMP_NUM_THREADS=1
source ~/bin/deepmd/deepmd-2.2.9.sh

mpirun -np $SLURM_NTASKS lmp -in lmp.in > lmp.out
cd ../2x2x2 && sbatch job.sh

echo "Job $SLURM_JOB_ID done at " `date`
