#!/bin/bash
for i in {1..9} {10..18};do
j=$((i+1))
rm -rf ${i}x${i}x${i} && mkdir ${i}x${i}x${i} && cd ${i}x${i}x${i}
cat > run.in << EOF
replicate   $i  $i  $i
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
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --gpus-per-task=1
#SBATCH -x gn[203]
#SBATCH --exclusive

module purge
module load GPUMD/4.6

echo "Starting job \$SLURM_JOB_ID at " \`date\`
echo "SLURM_SUBMIT_DIR is \$SLURM_SUBMIT_DIR"
echo "Running on nodes: \$SLURM_NODELIST"

gpumd > 4090_out
cd ../${j}x${j}x${j} && sbatch job.sh

echo "Job \$SLURM_JOB_ID done at " \`date\`
EOF
ln -fs ../../../216_water/model.xyz .
cd ..
done
