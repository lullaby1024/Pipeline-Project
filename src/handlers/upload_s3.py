import tornado.web
import boto3
from botocore.client import Config
# from src.s3.client import set_config


class UploadHandler(tornado.web.RequestHandler):

    def post(self):

        file = self.request.files['image_file'][0]

        if file is not None:
            # file_path = './uploads/test.jpg'
            #
            # output_file = open(file_path, 'wb')
            # output_file.write(file['body'])
            # image = open(file_path, 'rb')

            # Upload image to s3
            # key_name = 'test.' + file['filename'].split('.')[1]
            ACCESS_KEY_ID = 'AKIAJXFWIJSEUEELIH2Q'
            ACCESS_SECRET_KEY = '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'

            s3 = boto3.resource('s3',
                                aws_access_key_id=ACCESS_KEY_ID,
                                aws_secret_access_key=ACCESS_SECRET_KEY,
                                config=Config(signature_version='s3v4'))

            s3.Bucket('recipecialist').put_object(Key='test.jpg', Body=file['body'])
            # bucket = client.Bucket()
            # key_name = 'test.jpg'
            #
            # # ExtraArgs = {"ContentType": "image/jpeg"}

            self.finish("file " + file['filename'] + " is uploaded.")




