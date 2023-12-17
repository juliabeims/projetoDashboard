from pymongo import MongoClient
from variables import *

client = MongoClient(uri)
database = client["DatabaseData"]
collection = database["tableData"]

# Deletando todos os documentos da coleção
collection.delete_many({})

print("Documentos deletados!")
