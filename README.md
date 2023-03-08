# Baur et al The Deployment Length of Solar Radiation Modification: An Interplay of Mitigation, Net-negative Emissions and Climate Uncertainty 

[![DOI](https://zenodo.org/badge/611173270.svg)](https://zenodo.org/badge/latestdoi/611173270)



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




