import tornado.web
from util import Event

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

#read data from Google Cloud Platform
DB_USER = "zc2425"
DB_PASSWORD = "TXePyLYulh"
DB_SERVER = "w4111.cisxo09blonu.us-east-1.rds.amazonaws.com"
DATABASEURI = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_SERVER+"/w4111"

engine = create_engine(DATABASEURI)


#input:['chicken']
#output: {title:..., ingred:..., instructions:...}
def query(ingredients):

    ingredient = ingredients[0]
    cml = "SELECT * FROM recipes WHERE lower(ingredients) LIKE '%" + ingredient.lower() + "%'"
    result = g.conn.execute(text(cml))

    title = []
    ingred = []
    instructions = []
    #output_table = {}

    for line in  result:
      title.append(line['title'])
      ingred.append(line['ingredients'])
      instructions.append(line['instructions'])

    output_table = dict(title=title, ingredients=ingred, instructions = instructions)

    return output_table
