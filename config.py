import os

class Config(object):
    UPLOAD_PATH = os.environ.get("UPLOAD_PATH")