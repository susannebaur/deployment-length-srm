#!/bin/bash

#conda activate baur-et-al-srm-commitment

START=$1
END=$2

for i in $(seq $START $END)
do
papermill 001_derive-forcing-adjustment-single-ensemble-member.ipynb -p ENSEMBLE_MEMBER $i papermill_output/"output_${i}.ipynb"
done

