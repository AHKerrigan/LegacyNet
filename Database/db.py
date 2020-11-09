# Python-Sqlite cemetery database.
# this file will provide all backend functionalities for the databse-editing gui.
# table requirements: headstone id (count or rng), row, col, headstone bbox-global coord (four-corners), headstone centroid.

import sqlite3
import re
import json
import pandas as pd

# change database name here, to apply functions to a different database.
cemetery = "cemetery.db"

# validate cemetery name before inserting into table.
def isValidCemetery(cemetery_name: str) -> bool:
    pattern = re.compile('^[a-zA-Z ]+$')
    if cemetery_name and re.match(pattern, cemetery_name):
        return True
    return False

# validate headstone id before inserting into table.
def isValidID(id: str) -> bool:
    pattern = re.compile('^[0-9]+$')
    if id and re.match(pattern, id):
        return True
    return False

# validate headstone row's and col's before inserting into table.
def isValidOrder(rc: str) -> bool:
    pattern = re.compile('^[0-9a-zA-Z -]+$')
    if rc and re.match(pattern, rc):
        return True
    return False 

# validate headstone coordinates and centroid before inserting into table.
def isValidCoord(coord: str) -> bool:
    pattern = re.compile('^[+-]*[0-9]*[.][0-9]+$')
    if coord and re.match(pattern, coord):
        return True
    return False

# validate whether input is a valid feature in table.
def isValidFeature(feature: str) -> bool:
    features = set(['id', 'row', 'col', 'toplx', 'toply', 'toprx', 'topry', 'botlx', 'botly', 'botrx', 'botry', 'centroidx', 'centroidy']) 
    if feature and feature in features:
        return True
    return False

# validate whether input is a valid geojson file type.
def isValidGeoJSON(filename: str) -> bool:
    pattern = re.compile('^[a-zA-Z0-9 -_]+.geojson$')
    if filename and re.match(pattern, filename):
        return True
    return False

# get all current tables in database.
def getTables() -> list:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    conn.commit()
    conn.close()
    list_of_tables = []
    for table in tables:
        list_of_tables.append(table[0])
    return list_of_tables

# get all current id's in select table.
def getIDs(tablename: str) -> list:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT id FROM {tablename};")
    ids = c.fetchall()
    conn.commit()
    conn.close()
    list_of_ids = []
    for hid in ids:
        list_of_ids.append(str(hid[0]))
    return list_of_ids

# get row from specific headstone.
def getRow(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT row FROM {tablename} WHERE id = {hid};")
    row = c.fetchone()
    conn.commit()
    conn.close()
    return str(row[0])

# get col from specific headstone.
def getCol(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT col FROM {tablename} WHERE id = {hid};")
    col = c.fetchone()
    conn.commit()
    conn.close()
    return str(col[0])

# get toplx from specific headstone.
def getToplx(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT toplx FROM {tablename} WHERE id = {hid};")
    toplx = c.fetchone()
    conn.commit()
    conn.close()
    return str(toplx[0])

# get toply from specific headstone.
def getToply(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT toply FROM {tablename} WHERE id = {hid};")
    toply = c.fetchone()
    conn.commit()
    conn.close()
    return str(toply[0])

# get toprx from specific headstone.
def getToprx(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT toprx FROM {tablename} WHERE id = {hid};")
    toprx = c.fetchone()
    conn.commit()
    conn.close()
    return str(toprx[0])

# get topry from specific headstone.
def getTopry(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT topry FROM {tablename} WHERE id = {hid};")
    topry = c.fetchone()
    conn.commit()
    conn.close()
    return str(topry[0])

# get botlx from specific headstone.
def getBotlx(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT botlx FROM {tablename} WHERE id = {hid};")
    botlx = c.fetchone()
    conn.commit()
    conn.close()
    return str(botlx[0])

# get botly from specific headstone.
def getBotly(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT botly FROM {tablename} WHERE id = {hid};")
    botly = c.fetchone()
    conn.commit()
    conn.close()
    return str(botly[0])

# get botrx from specific headstone.
def getBotrx(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT botrx FROM {tablename} WHERE id = {hid};")
    botrx = c.fetchone()
    conn.commit()
    conn.close()
    return str(botrx[0])

# get botry from specific headstone.
def getBotry(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT botry FROM {tablename} WHERE id = {hid};")
    botry = c.fetchone()
    conn.commit()
    conn.close()
    return str(botry[0])

# get centroidx from specific headstone.
def getCentroidx(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT centroidx FROM {tablename} WHERE id = {hid};")
    centroidx = c.fetchone()
    conn.commit()
    conn.close()
    return str(centroidx[0])

# get centroidy from specific headstone.
def getCentroidy(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT centroidy FROM {tablename} WHERE id = {hid};")
    centroidy = c.fetchone()
    conn.commit()
    conn.close()
    return str(centroidy[0])

# NOTE: (input parameters might need changing) MAIN METHOD- populate table based on cemetery (enter filename and tablename, one-click create).
def populateTable(tablename: str, container: str) -> None:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        create = f'''CREATE TABLE IF NOT EXISTS {tablename} 
            (id INTEGER UNIQUE, row INTEGER, col INTEGER, 
            toplx FLOAT, toply FLOAT, toprx FLOAT, topry FLOAT, 
            botlx FLOAT, botly FLOAT, botrx FLOAT, botry FLOAT,
            centroidx FLOAT, centroidy FLOAT);'''
        c.execute(create)
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    for row in container:
        insert = f"INSERT OR REPLACE INTO {tablename} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"
        c.execute(insert, row)
    conn.commit()
    conn.close()

# create a table.
def createTable(tablename: str) -> None:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        create = f'''CREATE TABLE IF NOT EXISTS {tablename} 
            (id INTEGER UNIQUE, row INTEGER, col INTEGER, 
            toplx FLOAT, toply FLOAT, toprx FLOAT, topry FLOAT, 
            botlx FLOAT, botly FLOAT, botrx FLOAT, botry FLOAT,
            centroidx FLOAT, centroidy FLOAT);'''
        c.execute(create)
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    conn.commit()
    conn.close()

# delete an enitre table.
def deleteTable(tablename: str) -> None:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        delete = f"DROP TABLE IF EXISTS {tablename};"
        c.execute(delete)
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    conn.commit()
    conn.close()

# add a table entry.
def addEntry(tablename: str, id: int, row: int, col: int, toplx: float, toply: float, toprx: float, topry: float, botlx: float, botly: float, botrx: float, botry: float, centroidx: float, centroidy: float) -> None:
    #id, row, col, toplx, toply, toprx, topry, botlx, botly, botrx, botry, centroidx, centroidy = values.split(',')
    if not isValidCemetery(tablename):
        return
    if not isValidID(id):
        return
    if not isValidOrder(row) or not isValidOrder(col):
        return 
    if not isValidCoord(toplx) or not isValidCoord(toply) or not isValidCoord(toprx) or not isValidCoord(topry) or not isValidCoord(botlx) or not isValidCoord(botly) or not isValidCoord(botrx) or not isValidCoord(botry) or not isValidCoord(centroidx) or not isValidCoord(centroidy):
        return
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        add = f"INSERT OR REPLACE INTO {tablename} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"
        c.execute(add, (id, row, col, toplx, toply, toprx, topry, botlx, botly, botrx, botry, centroidx, centroidy))
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    conn.commit()
    conn.close()

# edit a table entry based on headstone id.
def editEntry(tablename: str, id: int, row: int, col: int, toplx: float, toply: float, toprx: float, topry: float, botlx: float, botly: float, botrx: float, botry: float, centroidx: float, centroidy: float) -> None:
    #row, col, toplx, toply, toprx, topry, botlx, botly, botrx, botry, centroidx, centroidy = values.split(',')
    if not isValidCemetery(tablename):
        return
    if not isValidID(id):
        return 
    if not isValidOrder(row) or not isValidOrder(col):
        return 
    if not isValidCoord(toplx) or not isValidCoord(toply) or not isValidCoord(toprx) or not isValidCoord(topry) or not isValidCoord(botlx) or not isValidCoord(botly) or not isValidCoord(botrx) or not isValidCoord(botry) or not isValidCoord(centroidx) or not isValidCoord(centroidy):
        return
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        edit = f"UPDATE {tablename} SET row = ?, col = ?, toplx = ?, toply = ?, toprx = ?, topry = ?, botlx = ?, botly = ?, botrx = ?, botry = ?, centroidx = ?, centroidy = ? WHERE id = ?" 
        c.execute(edit, (row, col, toplx, toply, toprx, topry, botlx, botly, botrx, botry, centroidx, centroidy, id))
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    conn.commit()
    conn.close()

# delete a table entry based on headstone id.
def deleteEntry(tablename: str, id: int) -> None:
    if not isValidID(id):
        return 
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        delete = f"DELETE FROM {tablename} WHERE id = ?;" 
        c.execute(delete, (id,))
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    conn.commit()
    conn.close()

# search table entries by ID.
def searchTable(tablename: str, start_id: str, finish_id) -> list:
    if not isValidID(start_id) or not isValidID(finish_id):
        return
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        search = f"SELECT * FROM {tablename} WHERE id BETWEEN ? AND ?;"
        c.execute(search, (start_id, finish_id))
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    entries = c.fetchall()
    result = []
    for entry in entries:
        result.append(entry)
    conn.commit()
    conn.close()
    return result

# view/order table with specified feature.
def orderTable(tablename: str, feature: str, sort: str) -> list:
    if sort.lower() == "asc" or sort.lower() == "desc":
        pass
    else:
        return
    if not isValidFeature(feature):
        return
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        order = f"SELECT * FROM {tablename} ORDER BY {feature} {sort};"
        c.execute(order)
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    entries = c.fetchall()
    result = []
    for entry in entries:
        result.append(entry)
    conn.commit()
    conn.close()
    return result

# convert a pandas dataframe into gejson format.
def df_to_geojson(df, properties, toplx = 'toplx', toply = 'toply', toprx = 'toprx', topry = 'topry', botlx = 'botlx', botly = 'botly', botrx = 'botrx', botry = 'botry', centroidx = 'centroidx', centroidy = 'centroidy') -> dict:
    geojson = {'type':'FeatureCollection', 'name': '', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature', 'properties':{}, 'geometry':{'type':'MultiPolygon', 'coordinates':[]}}
        feature['geometry']['coordinates'] = [[[row[toplx], row[toply]],[row[toprx], row[topry]], [row[botlx], row[botly]], [row[botrx], row[botry]], [row[toplx], row[toply]]]]
        for prop in properties:
            if prop == 'id' or prop == 'row' or prop == 'col':
                feature['properties'][prop] = int(row[prop])
            elif prop == 'centroid':
                feature['properties'][prop] = [row[centroidx], row[centroidy]]
            else:
                feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson

# store entries in a pandas dataframe, export table to geojson file.
def exportTable(tablename: str) -> None:
    output_filename = tablename + '.geojson'
    conn = sqlite3.connect(cemetery)
    try:
        df = pd.read_sql_query(f"SELECT * FROM {tablename}", conn)
    except conn.Error as e:
        conn.commit()
        conn.close()
        #print(e)
        return
    except:
        conn.commit()
        conn.close()
        #print("Unknown Error Occured")
        return
    conn.commit()
    conn.close()
    properties = ['id', 'row', 'col', 'centroid']
    geojson = df_to_geojson(df, properties)
    with open(output_filename, 'w') as output_file:
        json.dump(geojson, output_file, indent = 2)

# test functions.
# print(isValidCemetery("ce"))
# print(isValidID("0099887"))
# print(isValidOrder("1000"))
# print(isValidCoord("-000006.7"))
# print(createTable("test"))
# print(addEntry("test", "119887","17","23","+11.1999000456789","-10.1123123123123","-23.2000111111111","+32.21112229907","-03.3333333333333","+3.3333333333333","-41.477777777777790","-4.47777777779990","50.660606060606060","5.660606060606060"))
# print(addEntry("test", "5","17","23","+11.1999000456789","-10.1123123123123","-23.2000111111111","+32.21112229907","-03.3333333333333","+3.3333333333333","-41.477777777777790","-4.47777777779990","50.660606060606060","5.660606060606060"))
# print(addEntry("test", "105","17","23","+11.1999000456789","-10.1123123123123","-23.2000111111111","+32.21112229907","-03.3333333333333","+3.3333333333333","-41.477777777777790","-4.47777777779990","50.660606060606060","5.660606060606060"))
# print(addEntry("test", "12058", "100", "101", "1.10", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19"))
# print(editEntry("test", "0099887", "16","22","+11.1999000456789","-10.1123123123123","-23.2000111111111","+32.21112229907","-03.3333333333333","+3.3333333333333","-41.477777777777790","-4.47777777779990","50.660606060606060","5.660606060606060"))
# print(deleteEntry("test", "1111111"))
# print(searchTable("test", "1", "10"))
# print(orderTable("test", "id", "DESC"))
# print(orderTable("test", "id", "ASC"))
# print(exportTable("test"))
# print(getTables())