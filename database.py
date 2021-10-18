from urllib.parse import quote_plus
from pymongo import MongoClient
from settings import DATABASES
from datetime import datetime


class Mongo:
    def __init__(self, user=None, password=None, host=None, port=None, collection=None):
        host = host and host or DATABASES.get("host")
        port = port and port or int(DATABASES.get("port"))
        collection = collection and collection or DATABASES.get("collection")
        user = user and user or DATABASES.get("user")
        password = (
            password
            and qutoe_plus(str(password))
            or quote_plus(str(DATABASES.get("password")))
        )

        self.client = MongoClient(
            f"mongodb+srv://{user}:{password}@{host}?retryWrites=true&w=majority",
            int(port),
        )
        self.db = self.client.get_database(collection)
