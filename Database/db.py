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
    features = set(['id', 'row', 'col', 'coord1x', 'coord1y', 'coord2x', 'coord2y', 'coord3x', 'coord3y', 'coord4x', 'coord4y', 'centx', 'centy']) 
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

# get coord1x from specific headstone.
def getCoord1x(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord1x FROM {tablename} WHERE id = {hid};")
    coord1x = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord1x[0])

# get coord1y from specific headstone.
def getCoord1y(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord1y FROM {tablename} WHERE id = {hid};")
    coord1y = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord1y[0])

# get coord2x from specific headstone.
def getCoord2x(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord2x FROM {tablename} WHERE id = {hid};")
    coord2x = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord2x[0])

# get coord2y from specific headstone.
def getCoord2y(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord2y FROM {tablename} WHERE id = {hid};")
    coord2y = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord2y[0])

# get coord3x from specific headstone.
def getCoord3x(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord3x FROM {tablename} WHERE id = {hid};")
    coord3x = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord3x[0])

# get coord3y from specific headstone.
def getCoord3y(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord3y FROM {tablename} WHERE id = {hid};")
    coord3y = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord3y[0])

# get coord4x from specific headstone.
def getCoord4x(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord4x FROM {tablename} WHERE id = {hid};")
    coord4x = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord4x[0])

# get coord4y from specific headstone.
def getCoord4y(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT coord4y FROM {tablename} WHERE id = {hid};")
    coord4y = c.fetchone()
    conn.commit()
    conn.close()
    return str(coord4y[0])

# get centx from specific headstone.
def getCentx(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT centx FROM {tablename} WHERE id = {hid};")
    centx = c.fetchone()
    conn.commit()
    conn.close()
    return str(centx[0])

# get centy from specific headstone.
def getCenty(tablename: str, hid: int) -> str:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    c.execute(f"SELECT centy FROM {tablename} WHERE id = {hid};")
    centy = c.fetchone()
    conn.commit()
    conn.close()
    return str(centy[0])

# NOTE: (input parameters might need changing) MAIN METHOD- populate table based on cemetery (enter filename and tablename, one-click create).
def populateTable(tablename: str, container: str) -> None:
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        create = f'''CREATE TABLE IF NOT EXISTS {tablename} 
            (id INTEGER UNIQUE, row INTEGER, col INTEGER, 
            coord1x FLOAT, coord1y FLOAT, coord2x FLOAT, coord2y FLOAT, 
            coord3x FLOAT, coord3y FLOAT, coord4x FLOAT, coord4y FLOAT,
            centx FLOAT, centy FLOAT);'''
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
            coord1x FLOAT, coord1y FLOAT, coord2x FLOAT, coord2y FLOAT, 
            coord3x FLOAT, coord3y FLOAT, coord4x FLOAT, coord4y FLOAT,
            centx FLOAT, centy FLOAT);'''
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
def addEntry(tablename: str, hid: int, row: int, col: int, coord1x: float, coord1y: float, coord2x: float, coord2y: float, coord3x: float, coord3y: float, coord4x: float, coord4y: float, centx: float, centy: float) -> None:
    #id, row, col, coord1x, coord1y, coord2x, coord2y, coord3x, coord3y, coord4x, coord4y, centx, centy = values.split(',')
    if not isValidCemetery(tablename):
        return
    if not isValidID(hid):
        return
    if not isValidOrder(row) or not isValidOrder(col):
        return 
    if not isValidCoord(coord1x) or not isValidCoord(coord1y) or not isValidCoord(coord2x) or not isValidCoord(coord2y) or not isValidCoord(coord3x) or not isValidCoord(coord3y) or not isValidCoord(coord4x) or not isValidCoord(coord4y) or not isValidCoord(centx) or not isValidCoord(centy):
        return
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        add = f"INSERT OR REPLACE INTO {tablename} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"
        c.execute(add, (hid, row, col, coord1x, coord1y, coord2x, coord2y, coord3x, coord3y, coord4x, coord4y, centx, centy))
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
def editEntry(tablename: str, hid: int, row: int, col: int, coord1x: float, coord1y: float, coord2x: float, coord2y: float, coord3x: float, coord3y: float, coord4x: float, coord4y: float, centx: float, centy: float) -> None:
    #row, col, coord1x, coord1y, coord2x, coord2y, coord3x, coord3y, coord4x, coord4y, centx, centy = values.split(',')
    if not isValidCemetery(tablename):
        return
    if not isValidID(hid):
        return 
    if not isValidOrder(row) or not isValidOrder(col):
        return 
    if not isValidCoord(coord1x) or not isValidCoord(coord1y) or not isValidCoord(coord2x) or not isValidCoord(coord2y) or not isValidCoord(coord3x) or not isValidCoord(coord3y) or not isValidCoord(coord4x) or not isValidCoord(coord4y) or not isValidCoord(centx) or not isValidCoord(centy):
        return
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        edit = f"UPDATE {tablename} SET row = ?, col = ?, coord1x = ?, coord1y = ?, coord2x = ?, coord2y = ?, coord3x = ?, coord3y = ?, coord4x = ?, coord4y = ?, centx = ?, centy = ? WHERE id = ?" 
        c.execute(edit, (row, col, coord1x, coord1y, coord2x, coord2y, coord3x, coord3y, coord4x, coord4y, centx, centy, hid))
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
def deleteEntry(tablename: str, hid: int) -> None:
    if not isValidID(hid):
        return 
    conn = sqlite3.connect(cemetery)
    c = conn.cursor()
    try:
        delete = f"DELETE FROM {tablename} WHERE id = ?;" 
        c.execute(delete, (hid,))
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
def df_to_geojson(df, properties, coord1x = 'coord1x', coord1y = 'coord1y', coord2x = 'coord2x', coord2y = 'coord2y', coord3x = 'coord3x', coord3y = 'coord3y', coord4x = 'coord4x', coord4y = 'coord4y', centx = 'centx', centy = 'centy') -> dict:
    geojson = {'type':'FeatureCollection', 'name': '', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature', 'properties':{}, 'geometry':{'type':'MultiPolygon', 'coordinates':[]}}
        feature['geometry']['coordinates'] = [[[row[coord1x], row[coord1y]],[row[coord2x], row[coord2y]], [row[coord3x], row[coord3y]], [row[coord4x], row[coord4y]], [row[coord1x], row[coord1y]]]]
        for prop in properties:
            if prop == 'id' or prop == 'row' or prop == 'col':
                feature['properties'][prop] = int(row[prop])
            elif prop == 'centroid':
                feature['properties'][prop] = [row[centx], row[centy]]
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
    print(df)
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