from rpy2.robjects import r
from pathlib import Path
from runr.convert import rpy2_to_pandas
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent


def runr(rscript):
    rscript = "\n".join(rscript.splitlines())
    script_result = r(rscript)
    result_table = format_table(script_result)
    return result_table


def format_table(script_result):
    data = pd.DataFrame(rpy2_to_pandas(script_result))
    num_col = len(data.columns)
    num_row = len(data)
    names_col = data.columns[:].tolist()

    for x in data:
        data[x] = data[x].astype(str)

    for x in range(num_row):
        data.iloc[0:num_row, x:(x + 1)] = data.iloc[0:num_row, x:(x + 1)] + '_'

    for x in range(num_col):
        names_col[x] = names_col[x] + '_'

    data.columns = names_col

    for x in names_col:
        data[x] = data[x].str.strip()

    for x in names_col:
        data[x] = data[x].str.lstrip()

    data = data.iloc[:, 1:]

    data_string = data.to_string(index=False)

    html_table = gen_html_table(data_string)

    return html_table


def gen_html_table(data_string):
    string_table = data_string
    thead = 0
    html_table = f"<table class=\"table table-striped\">"
    for line in string_table.splitlines():
        if thead == 0:
            html_table += f"<thead>"
        else:
            pass
        for n in line.split("_"):
            html_table += f"<td>{n}</td>"
        if thead == 0:
            html_table += f"</thead>"
        else:
            pass
        html_table += "<tr>"
        thead += 1
    html_table += "</table>"
    return html_table
