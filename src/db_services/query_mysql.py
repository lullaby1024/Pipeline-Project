import pymysql

def query(ingr):
    cnx = pymysql.connect(host='localhost',
                          user='root',
                          password='dbuserdbuser',
                          db='pipeline_project',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)

    cursor = cnx.cursor()

    q = "SELECT * FROM recipes WHERE lower(ingredients) LIKE " + "'%" + ingr.lower() + "%'"
    result = cursor.execute(q)
    result = cursor.fetchall()

    cnx.commit()
    cnx.close()

    return result