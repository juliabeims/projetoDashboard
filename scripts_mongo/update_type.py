from pymongo import MongoClient
from variables import *

client = MongoClient(uri)
database = client["DatabaseData"]
collection = database["tableData"]

# Atualizando o tipo dos campos de data para ISODate
collection.update_many({}, [{'$set': {'tempo_fim_teste': {'$toDate': '$tempo_inicio_teste'}}}])

print("Conversão de tipo concluída!")
