#!/bin/sh
#SBATCH -p 4090
#SBATCH -J PdCuNiP
#SBATCH -N 1
#SBATCH -o out
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --gpus-per-task=1
#SBATCH -w gn202

module purge
module load GPUMD/4.6

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

nep
python ~/bin/GPUMD/train_plot.py

echo "Job $SLURM_JOB_ID done at " `date`
