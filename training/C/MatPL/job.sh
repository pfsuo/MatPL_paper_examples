#!/bin/sh
#SBATCH -p 4090
#SBATCH -J C
#SBATCH -N 1
#SBATCH -o out
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --gpus-per-task=1
#SBATCH -w gn204

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

source /share/app/MATPL/MatPL-2025.3/env.sh
for a i in {1..15};do
MatPL train input.json
done
cd test && MatPL test test.json

echo "Job $SLURM_JOB_ID done at " `date`
