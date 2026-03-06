#!/bin/bash
for i in {1..20};do
j=$((i+1))
mkdir ${i} && cd ${i}
cat > run.in << EOF
replicate   $i  $(($i*2))  $(($i*2))
velocity    300
potential   /data/home/pfsuo/pfsuo/software/build/nep-data/2023_Xu_liquid_water/nep.txt
ensemble nvt_nhc 300 300 100
time_step   0.5
dump_thermo 100
run         10000
EOF
cat > job.sh << EOF
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

echo "Starting job \$SLURM_JOB_ID at " \`date\`
echo "SLURM_SUBMIT_DIR is \$SLURM_SUBMIT_DIR"
echo "Running on nodes: \$SLURM_NODELIST"

/data/home/pfsuo/pfsuo/software/GPUMD-4.9/src/gpumd > 4090_out
cd ../${j} && sbatch job.sh

echo "Job \$SLURM_JOB_ID done at " \`date\`
EOF
ln -fs ../../../216_water/model.xyz .
if [ $i -eq 1 ]; then
sbatch job.sh
fi
cd ..
done
