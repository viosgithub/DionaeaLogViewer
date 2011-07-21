import sqlite3
import wx

INDENT = 4
TABLE_LIST = ("dcerpcbinds","dcerpcrequests","emu_profiles","emu_services_old",
"offers","downloads","resolves","p0fs","logins","mssql_fingerprints",
"mssql_commands","mysql_commands","emu_services")

def getData(num=5,localPort="",remoteIP="",gauge=None):
    #curMain.execute("select * from connections where local_port = %s and remote_host = %s" % (localPort,remoteIP))
    ret = ""
    curMain.execute("select * from connections")
    i = 0
    for rowConnections in curMain:
        if localPort != "":
            if rowConnections[8] != localPort:
                continue
        if remoteIP != "":
            if rowConnections[9] != remoteIP:
                continue
        i += 1
        if gauge:
            gauge.SetValue(i)
        if i > num:
            break
        ret += "*" * 15 + "\n"
        ret += 'table:"%s"' % "connections\n"
        count = 0
        for column in tableInfo["connections"]:
            ret += " " * INDENT + "%s:%s\n" % (column[1],str(rowConnections[count]))
            count += 1
    
        for table in TABLE_LIST:
            ret += "\n"
            curSub.execute("select * from %s where connection = %d" % (table,rowConnections[0]))
            ret += 'table:"%s"\n' % table
            for columnList in curSub:
                count = 0
                for column in columnList:
                    if tableInfo[table][count][1] != "connection" :
                        ret += " " * INDENT + "%s:%s\n" % (tableInfo[table][count][1],str(column))
                    count += 1
    return ret

con = sqlite3.connect("logsql.sqlite")

tableList = []
tableInfo = {}
curMain = con.cursor()
curSub = con.cursor()

curMain.execute("select name from sqlite_master where type='table'")
for catalog in curMain.fetchall():
    tableList.append(catalog[0])

for table in tableList:
    curMain.execute("PRAGMA table_info(%s)"  % table)
    columnList = curMain.fetchall()
    tableInfo.update({table:columnList})




