import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://dhananjayg4:ddg1992@cluster92.t8e4svk.mongodb.net/?retryWrites=true&w=majority"
)

db = client.test
print(db)

d = {
    "name": "Dhananjay_1",
    "surname": "Gavale_1",
    "Email-id": "dhannanjayg4@gmail.com"
}

db1 = client['mongotrail']
coll = db1['test3']
coll.insert_one(d)
