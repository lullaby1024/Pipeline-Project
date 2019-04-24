import tornado.ioloop
import tornado.web
import logging
import os

from src.db_services.image import get_image
from src.db_services.query import query
from src.model_services.label_image import predict_label


class MainHandler(tornado.web.RequestHandler):
    def run_model(self):
        # CAVEAT: local executions
        image_path = get_image()
        query_ingr = predict_label(image_path) # list of ingredients
        results = query(query_ingr)  # dictionary

        self.render("html/recommendation.html", data=results)


class Application(tornado.web.Application):
    def __init__(self):
        # TODO: online executions (API)
        app_settings = {
            'default_handler_args': dict(status_code=404),
            'static_path': os.path.join(os.path.dirname(__file__), 'static')
        }

        app_handlers = [

            (r'^/$', MainHandler)

        ]

        super(Application, self).__init__(app_handlers, **app_settings)


if __name__ == "__main__":
    port = 8888
    address = '0.0.0.0'
    logging_level = logging.getLevelName('INFO')
    logging.getLogger().setLevel(logging_level)
    logging.info('starting foo_web_ui on %s:%d', address, port)

    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(), xheaders=True)
    http_server.listen(port, address=address)

    tornado.ioloop.IOLoop.instance().start()