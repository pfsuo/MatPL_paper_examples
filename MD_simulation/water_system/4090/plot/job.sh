#!/bin/sh
#SBATCH -p cpu,cpu3
#SBATCH -J plot
#SBATCH -d afterok:3900543
#SBATCH -N 1
#SBATCH --ntasks-per-node=1

python plot.py
