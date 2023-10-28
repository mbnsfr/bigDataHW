import pymongo
import pandas as pd

# get collection
client = pymongo.MongoClient(
    'mongodb://localhost:27017')
db = client['proj1']
collection = db['gym']

# find
# data = collection.find({'day_of_week': 4})

# sort
# data = collection.aggregate([
#     {'$sort': {'date': 1}}
# ])

# match and count
# data = collection.aggregate(
#     [{'$match': {'month': 8}}, {'$count': 'number_people'}])

# group and count
# data = collection.aggregate(
#     [{'$group': {
#         '_id': '$day_of_week',
#         'population': {'$sum': '$number_people'}
#     }}])

# match and group and sum
# data = collection.aggregate(
#     [{
#         '$match': {'$and': [
#             {'hour': {'$gte': 17}},
#             {'hour': {'$lte': 20}}
#         ]}
#     },
#         {
#         '$group': {
#             '_id': '$month',
#             'population': {'$sum': "$number_people"}
#         }
#     }
#     ])

# match and group and sort
# data = collection.aggregate(
#     [{
#         '$match': {'$and': [
#             {'hour': {'$gte': 17}},
#             {'hour': {'$lte': 20}}
#         ]}
#     },
#         {
#         '$group': {
#             '_id': '$month',
#             'population': {'$avg': "$number_people"}
#         }
#     }
#     ])

# saving
df = pd.DataFrame(data)
df.to_csv('/home/mbnsfr/Desktop/bd/sample.csv')
