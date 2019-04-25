import tornado.web

class UploadHandler(tornado.web.RequestHandler):
    def post(self):

        file = self.request.files['image_file'][0]

        output_file = open("uploads/" + file['filename'], 'wb')
        output_file.write(file['body'])

        self.finish("file " + file['filename'] + " is uploaded")
