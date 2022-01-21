from rpy2.robjects import r
from runr.convert import rpy2_to_pandas
import pandas as pd
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def execute(script):
    script_text = "\n".join(script.splitlines())
    script_result = r(script_text)
    filename = save_file(script_result)
    result_table = format_table(script_result)
    return result_table, filename


def save_file(script_result):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    dir_filename = f"runr/export/df_" + timestamp + ".xlsx"
    filename = f"df_" + timestamp + ".xlsx"
    dataframe_result = pd.DataFrame(rpy2_to_pandas(script_result))
    dataframe_result.to_excel(dir_filename)
    return filename


def format_table(script_result):
    dataframe = pd.DataFrame(rpy2_to_pandas(script_result))
    if dataframe.columns[0] == 0:
        dataframe = dataframe.rename(columns={dataframe.columns[0]: "UnnamedColumn"})
    dataframe.insert(0, 'Index', dataframe.index)
    html_table = gen_html_table(dataframe)
    return html_table


def gen_html_table(dataframe):

    index = list(dataframe['Index'])
    col_names = dataframe.columns[:].tolist()
    html_table = f"<table class=\"table table-striped table-hover\">"
    html_table += f"<thead>"
    for column in col_names:
        html_table += f"<th scope=\"col\">{column}</th>"
    html_table += f"</thead>"
    for row in index:
        html_table += "<tr>"
        for row_col in col_names:
            if row_col == 'Index':
                html_table += f"<th scope = \"row\">{dataframe.loc[row, row_col]}</td>"
            else:
                html_table += f"<td>{dataframe.loc[row, row_col]}</td>"
        html_table += "</tr>"
    html_table += "</table>"
    return html_table

