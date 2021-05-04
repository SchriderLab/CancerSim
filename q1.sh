#!/bin/bash

#SBATCH --mem=10g
#SBATCH -t 02:00:00
#SBATCH --mail-type=END
#SBATCH --mail-user=amjad_dabi@unc.edu

slim NonWFCancer4.slim
