import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "english4", #put your password here
                           db = "demo")
    c = conn.cursor()

    return c, conn
