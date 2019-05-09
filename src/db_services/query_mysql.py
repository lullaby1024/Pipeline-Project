import pymysql
# from nltk.corpus import wordnet as wn


def query(ingredients):
    cnx = pymysql.connect(host='localhost',
                          user='root',
                          password='dbuserdbuser',
                          db='pipeline_project',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)

    cursor = cnx.cursor()
    #TODO: add database to s3 and connect
    #TODO: modify query and input

    # food = wn.synset('food.n.02')
    # food_dict = list(set([w for s in food.closure(lambda s: s.hyponyms()) for w in s.lemma_names()]))

    # Parse sql query.
    q = "SELECT * FROM recipes WHERE "
    for i in ingredients:
        if i == ingredients[-1]: # If i is the last element
            q += "ingredients LIKE '%" + i + "%'"
        else:
            q += "ingredients LIKE '%" + i + "%' OR "

    result = cursor.execute(q)
    result = cursor.fetchall()

    cnx.commit()
    cnx.close()

    return result