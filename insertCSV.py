import pymongo
import pandas as pd

# data from csv to dataframe
dir = '/home/mbnsfr/Desktop/bd/data/data.csv'
data = pd.read_csv(dir)

# Connect to MongoDB
client =  pymongo.MongoClient("mongodb://localhost:27017/")
db = client['proj1']
collection = db['gym']
data.reset_index(inplace=True)
data_dict = data.to_dict("records")

# Insert collection
collection.insert_many(data_dict)