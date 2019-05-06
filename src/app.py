import tornado.ioloop
import tornado.web
import logging
import os
import json


from src.db_services.query_mysql import query
from src.model_services.label_image import predict_label
from src.handlers.upload import UploadHandler

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index.html")

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        # CAVEAT: local executions
        img_path = './uploads/test_img.jpg'
        query_ingr = predict_label(img_path)  # list of ingredients
        # self.write(query_ingr)
        results = query(query_ingr)  # dictionary
        self.render("html/recommendation.html", data=results)

    def post(self):
        my_image = self.get_argument("desired image: ")


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
            (r'^/recommend$', MainHandler)

        ]

        super(Application, self).__init__(app_handlers, **app_settings)


if __name__ == "__main__":
    port = 7777
    address = '0.0.0.0'
    logging_level = logging.getLevelName('INFO')
    logging.getLogger().setLevel(logging_level)
    logging.info('starting foo_web_ui on %s:%d', address, port)

    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(), xheaders=True)
    http_server.listen(port, address=address)

    tornado.ioloop.IOLoop.instance().start()