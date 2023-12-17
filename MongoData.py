from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pandas as pd

class MongoData:
    def __init__ (self,uri):
        try:
            self.client = MongoClient(uri)
            self.client.admin.command('ismaster')
        except ConnectionFailure:
            print("Falha na conexão com o MongoDB. Verifique a URI fornecida.")
            self.client = None

    def filter_mongo(self,database,collection,start_date,end_date,suite_name="all"):
        self.database = self.client[database]
        self.collection = self.database[collection]

        if suite_name == "all":
             self.filter = self.collection.find({
            'tempo_inicio_teste': {'$gte': start_date, '$lte': end_date},
            })
        else:     
            self.filter = self.collection.find({
                'nome_suite': suite_name,
                'tempo_inicio_teste': {'$gte': start_date, '$lte': end_date},
            })

        self.filter_list = [post for post in self.filter]

        self.df = pd.DataFrame(self.filter_list)
        return self.df




