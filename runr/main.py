from rpy2.robjects import r, pandas2ri
import pandas as pd
import os


def runr():
    gameretr = r.source('runr/getsuperbowlresults.r')
    gamedata = (gameretr[gameretr.names.index('value')])
    superbowlresults = pandas2ri.rpy2py_dataframe(gamedata)
    result_tab_html = superbowlresults.to_html()
    return result_tab_html
