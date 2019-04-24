import tornado.web
from util import Event
import sys

class ImageHandler(tornado.web.RequestHandler):
    def get_image():
        path = input('Enter the image path')
        #path = sys.stdin.readline()
        return path
