import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://dhananjay:dhananjay92@cluster92.ec72xml.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Dhananjay",
    "surname": "Gavale",
    "Email-id": "dhannanjayg4@gmail.com"
}
db1 = client['mongotrail']
coll = db1['test']
coll.insert_one(d)