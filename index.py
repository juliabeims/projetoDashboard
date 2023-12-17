from MongoData import MongoData
from variables import *
from datetime import datetime

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,17)

Mongo = MongoData(uri)
df = Mongo.filter_mongo("DatabaseData","tableData",start_date,end_date,"Carrinho")

print(df)