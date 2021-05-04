#!/bin/bash
#SBATCH -t 01:00:00
#SBATCH --output=output.out
#SBATCH --error=err.out
slim ./tmp/temp_slim10.slim
