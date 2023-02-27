from pathlib import Path

import scmdata


ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
PLOTS_DIR = ROOT_DIR / "plots"


def clean_scenarios(inp):
    """
    Based on https://github.com/iiasa/climate-assessment/blob/main/src/climate_assessment/climate/wg3.py
    """
    inp = inp.filter(
        variable=[
            "*Infilled|Emissions|CO2",
            "*Infilled|Emissions|F-Gases",
            "*Infilled|Emissions|HFC",
            "*Infilled|Emissions|PFC",
            "*Infilled|Emissions|Kyoto Gases (AR5-GWP100)",
            "*Infilled|Emissions|Kyoto Gases (AR6-GWP100)",
        ],
        keep=False,
    )

    infilled_emms_filter = "*Infilled*"
    df_clean = inp.filter(variable=infilled_emms_filter).timeseries().reset_index()

    replacements_variables = {
        r".*\|Infilled\|": "",
        "AFOLU": "MAGICC AFOLU",
        "Energy and Industrial Processes": "MAGICC Fossil and Industrial",
        "HFC43-10": "HFC4310mee",
        r"HFC\|": "",
        r"PFC\|": "",
        "HFC245ca": "HFC245fa",
    }
    for old, new in replacements_variables.items():
        df_clean["variable"] = df_clean["variable"].str.replace(old, new, regex=True)

    replacements_units = {
        "HFC43-10": "HFC4310mee",
    }
    for old, new in replacements_units.items():
        df_clean["unit"] = df_clean["unit"].str.replace(old, new, regex=True)

    def fix_hfc_unit(variable):
        if "HFC" not in variable:
            raise NotImplementedError(variable)

        return "kt {}/yr".format(variable.split("|")[-1])

    hfc_rows = df_clean["variable"].str.contains("HFC")
    df_clean.loc[hfc_rows, "unit"] = df_clean.loc[hfc_rows, "variable"].apply(
        fix_hfc_unit
    )

    try:
        # if extra col is floating around, remove it
        df_clean = df_clean.drop("unnamed: 0", axis="columns")
    except KeyError:
        pass

    return scmdata.ScmRun(df_clean)
