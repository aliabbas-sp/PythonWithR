from rpy2.robjects import r, pandas2ri

GameRetR = r.source('GetSuperBowlResults.r')
GameData = (GameRetR[GameRetR.names.index('value')])
SuperBowlResults = pandas2ri.rpy2py_dataframe(GameData)
SuperBowlResults.to_excel("SuperBowlResults.xlsx", sheet_name='SuperBowlResults')