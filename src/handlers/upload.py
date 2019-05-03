import tornado.web

class UploadHandler(tornado.web.RequestHandler):

    def get(self):

        file = self.request.files['image_file'][0]

        output_file = open("../uploads/" + 'test_img', 'wb')
        output_file.write(file['body'])

        image_path = "../uploads/" + file['filename']

        self.finish("file " + file['filename'] + " is uploaded")



