#!/bin/sh
#SBATCH -p 4090
#SBATCH -J MACE_ase
#SBATCH -N 1
#SBATCH -o out
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --gpus-per-task=1
#SBATCH -w gn204

module purge

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

source /share/app/anaconda3/envs/MACE/env.sh
rm -f nose*
python run_md.py

echo "Job $SLURM_JOB_ID done at " `date`
