import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        self.url = url
        self.payload = payload

        resp = {"users": []}

        if self.url == "/users":
            for users in self.payload:
                return users



    def post(self, url, payload=None):
        pass
