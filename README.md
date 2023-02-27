# Baur et al Deployment Length of SRM

## Installation

### Required packages

Install conda or mamaba then run the following steps.

```sh
# create a new conda environment
mamba create --name baur-et-al-srm-commitment
# activate it
mamba activate baur-et-al-srm-commitment
# install dependencies
mamba env update --name baur-et-al-srm-commitment -f environment.yml
```

### Getting MAGICC7

MAGICC7 can be downloaded using the script `scripts/get-magicc.sh`.
Instructions for how to use this script are included in the script.

MAGICC7 and the parameter set are available from www.magicc.org.
After registering, you will be sent personal links for downloading.
These links are linked to your magicc.org account and can be used to download MAGICC.

Please read the license and expectations of using MAGICC carefully (available at https://magicc.org/download/magicc7), we rely on users to act in a way which brings both new scientific outcomes but also acknowledges the work put into the MAGICC AR6 setup.

### Setting up your environment

We use a `.env` file to store environment variables for running MAGICC.
To set yours up, copy the `.env.sample` file in this repository to `.env` and then update the paths to the settings you want to use.

### Commitment calculation
1. For each ensemble member calculate 1.5C trajectory (baur-et-al-srm-commitment/notebooks/001_*.ipynb) 
-> conda activate baur-et-al-srm-commitment
-> run with papermill (baur-et-al-srm-commitment/notebooks/run_001_forcing_adj.sh)
-> result (1.5C-ERF-pathways) is saved to /Users/baur/Documents/gitlab/zeb_git/baur-et-al-srm-commitment/magicc-bits-and-pieces/magicc-v7.5.3/run/15_ERF_trajectories/ -> symlink to baur-et-al-srm-commitment/data/15_ERF_trajectories
 (same for temperature pathways 15_T_trajectories)
-> run baur-et-al-srm-commitment/notebooks/002_*.ipynb to concatenate the 1.5-ERF-pathwys together, add climate sensitivity info and export as .csv (& to check result by plotting)
2. Create extension of each WG3 scenario until 2500 (baur-et-al-srm-commitment/notebooks/012_*.ipynb)
-> also adds yearly CDR, total CDR (until 2500) and cumulative emissions until net-zero to the metadata
3. Run extension of each WG3 scenario (baur-et-al-srm-commitment/notebooks/021_*.ipynb)
-> Group scenarios (SCENARIO_MIN and SCENARIO_MAX) to not run everything at once
-> Run with papermill (baur-et-al-srm-commitment/notebooks/run_021_extended_scenarios.sh)
4. Add total CDR until 1.5°C to the magicc output (T and ERF) from 3.  (baur-et-al-srm-commitment/notebooks/099_*.ipynb)
5. Calculate the difference in forcing between 1.5 trajectory (2.) and the WG3 scenario (3.) (baur-et-al-srm-commitment/notebooks/100_*.ipynb)
-> add peak warming and SRM time length to metadata
6. TO DO notebooks that prepare the data for plotting



