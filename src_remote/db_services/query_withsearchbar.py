# import pymysql
from sqlalchemy import create_engine
# from nltk.corpus import wordnet as wn
# from pyathena import connect


def query_search(ingredients):
    # cnx = pymysql.connect(host='localhost',
    #                       user='root',
    #                       password='dbuserdbuser',
    #                       db='pipeline_project',
    #                       charset='utf8mb4',
    #                       cursorclass=pymysql.cursors.DictCursor)
    #
    # cursor = cnx.cursor()

    # Connect to s3 database
    # bucket = 'recipecialist'
    #
    # cursor = connect(aws_access_key_id = ACCESS_KEY_ID,
    #                  aws_secret_access_key=ACCESS_KEY,
    #                  s3_staging_dir='s3://'+ bucket,
    #                  region_name='us-east-1',
    #                  cursorclass=pymysql.cursors.DictCursor).cursor()

    # Set up the DB credentials.
    DB_USER = "zc2425"
    DB_PASSWORD = "TXePyLYulh"
    DB_SERVER = "w4111.cisxo09blonu.us-east-1.rds.amazonaws.com"

    DATABASEURI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_SERVER + "/w4111"

    engine = create_engine(DATABASEURI)
    cnx = engine.raw_connection()
    cursor = cnx.cursor()

    #TODO: modify query and input

    # food = wn.synset('food.n.02')
    # food_dict = list(set([w for s in food.closure(lambda s: s.hyponyms()) for w in s.lemma_names()]))

    # Parse sql query.
    q = "SELECT * FROM recipes WHERE lower(ingredients) LIKE '%" + ingredients.lower() + "%'"
    #for i in ingredients:
        #if i == ingredients[-1]: # If i is the last element
            #q += "ingredients LIKE '%" + i + "%'"
        #else:
            #q += "ingredients LIKE '%" + i + "%' OR "

    result = cursor.execute(q)
    result = cursor.fetchall()

    cnx.commit()
    cnx.close()

    title = []
    ingredient = []
    insturctions = []

    for line in result:

        title.append(line[0])
        ingredient.append(line[1])
        insturctions.append(line[2])

    all_result = []
    for i in range(0, len(title)):
        one_result_row = []
        one_result_row.append(title[i])
        one_result_row.append(ingredient[i])
        one_result_row.append(insturctions[i])
        all_result.append(one_result_row)
        one_result_row = []

    # return result
    return all_result
