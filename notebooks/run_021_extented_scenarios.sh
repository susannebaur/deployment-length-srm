#!/bin/bash

#conda activate /data/scratch/globc/baur/baur-et-al-srm-commitment 

papermill 021_running-extended-scenarios-with-magicc.ipynb -p SCENARIOS_min $1 -p SCENARIOS_max $2 papermill_output/"output_magicc_run_${1}_${2}.ipynb"
