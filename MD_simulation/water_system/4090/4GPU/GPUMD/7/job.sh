#!/bin/sh
#SBATCH -p 4090
#SBATCH -J water
#SBATCH -N 1
#SBATCH -o out
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:4
#SBATCH --gpus-per-task=1
#SBATCH -w gn[202]

module purge
module load gcc/8.3.1 cuda/12.1-share

echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

/data/home/pfsuo/pfsuo/software/GPUMD-4.9/src/gpumd > 4090_out
cd ../8 && sbatch job.sh

echo "Job $SLURM_JOB_ID done at " `date`
