import tornado.web
from src_remote.db_services._query import query

class SearchHandler(tornado.web.RequestHandler):

    def post(self):
        ingredient_input = self.request.arguments['search_text'][0]
        ingredient_input = str(ingredient_input)[2:][:-1].split(',')  # list

        q_results = query(ingredient_input)  # dictionary

        self.render("../html/searched_recommendation.html", data=q_results)