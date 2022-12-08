#!/bin/bash -l
#SBATCH --partition=gpu-preempt
#SBATCH --time=12:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-task=1
#SBATCH --job-name=argo
#SBATCH --mem=65000
#SBATCH -o run-%j.out  # %j = job ID
#SBATCH --export=NONE

module purge
module load miniconda
python3 --version
which python3

conda activate /work/albertl_uri_edu/.conda/envs/f2f_2/
conda info --envs

python3 --version
which python3

pip list

conda list

python3 -u argo.py  > argo.out 