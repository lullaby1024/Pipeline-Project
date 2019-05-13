import tornado.ioloop
import tornado.web
import logging
import os
import json

from db_services.query_mysql import query
from db_services.query_withsearchbar import query_search
# from src.model_services.label_image import predict_label
# from src.handlers.upload import UploadHandler
from handlers.upload_s3 import UploadHandler
from model_services.label_image_s3 import detect_labels


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index_withsearchbar.html")


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        # img_path = './uploads/test_img.jpg'
        # img_url = 'http://s3-us-east-1.amazonaws.com/recipecialist/test_img.jpg'

        results = []
        query_ingr = detect_labels()  # list of ingredients
        results.append(query_ingr)
        # self.render("html/labeling.html", data=query_ingr)
        # self.write(query_ingr)
        q_results = query(list(query_ingr.keys()))  # dictionary
        results.append(q_results)

        self.render("html/recommendation.html", data=results)


class SearchHandler(tornado.web.RequestHandler):

    def post(self):
        
        ingredient_input = self.request.arguments['ingredient_search'][0]
        ingredient_input = str(ingredient_input)
        #ingredient_input = self.get_argument('ingredient_search')
        print(ingredient_input)
        results = []
        q_results = query_search(ingredient_input)  # dictionary
        results.append(q_results)

        self.render("html/searched_recommendation.html", data=results)


class Application(tornado.web.Application):
    def __init__(self):
        # TODO: online executions (API)
        app_settings = {
            'default_handler_args': dict(status_code=404),
            'static_path': os.path.join(os.path.dirname(__file__), 'static')
        }
        app_handlers = [
            (r'^/$', IndexHandler),
            (r'^/upload$', UploadHandler),
            (r'^/recommend$', MainHandler),
            (r'^/searchIngredient$', SearchHandler)

        ]

        super(Application, self).__init__(app_handlers, **app_settings)


if __name__ == "__main__":
    port = 8889
    address = '0.0.0.0'
    logging_level = logging.getLevelName('INFO')
    logging.getLogger().setLevel(logging_level)
    logging.info('starting foo_web_ui on %s:%d', address, port)

    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(), xheaders=True)
    http_server.listen(port, address=address)

    tornado.ioloop.IOLoop.instance().start()