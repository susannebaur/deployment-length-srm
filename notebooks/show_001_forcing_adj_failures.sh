#!/bin/bash

START=$1
END=$2

RERUN=True
# RERUN=False

counter=0
for i in $(seq $START $END)
do
    if [[ ! -f ../data/15_ERF_trajectories/"${i}_2030_EXTRA_RF.csv" ]]; then 
        echo "$i failed"
        
        if [[ $RERUN == "True" ]]; then
            echo "Re-running"
            counter=$((counter+1))
            papermill 001_derive-forcing-adjustment-single-ensemble-member.ipynb -p ENSEMBLE_MEMBER $i papermill_output/"output_${i}.ipynb" &
            sleep 0.5
            if (( counter > 10 )); then
                counter=0
                echo "Waiting"
                wait
            fi
        fi
    fi
done
wait
echo "All finished"
