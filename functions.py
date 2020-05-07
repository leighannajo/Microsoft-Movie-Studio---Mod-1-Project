import locale
def int_to_dollar(x):
    return locale.currency(x, grouping=True)
    
def dollar_to_int(dollar):
    #x = dollar.replace('$', "").replace(',', "")
    return float(dollar.replace('$', "").replace(',', ""))

def add_columns(x, y):
    if (x > 0) & (y > 0):
        return x + y
    else:
        return 0
    
def splitNewCol(dfName, columnName):
    newColumn = []
    for val in dfName[columnName]:
        newColumn.append(val.split(","))
    return(newColumn)

def removeFirstLastChar(dfName, columnName, char1, char2):
    newCol = []
    for val in dfName[columnName]:
        newCol.append(val.replace(char1, '').replace(char2, ''))
    return(newCol)

def countNewCol(dfName, columnName):
    newCount = []
    for val in dfName[columnName]:
        newCount.append(len(val))
    return(newCount)

def popularity(n):
    popularity = 0
    for i in df.index:
        if any(n in x for x in df['genre_list'][i]):
            popularity += (df['popularity'][i])
    return(popularity)

def count(n):
    count = 0
    for i in df.index:
        if any(n in x for x in df['genre_list'][i]):
            count += 1
    return(count)