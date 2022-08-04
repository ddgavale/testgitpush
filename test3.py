import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://dhananjayg4:ddg1992@cluster92.t8e4svk.mongodb.net/?retryWrites=true&w=majority"
)
db = client.test
print(db)
d = {
    "name": "Dhananjay_0",
    "surname": "Gavale_0",
    "Email-id": "dhannanjayg4@gmail.com"
}
db1 = client['mongotest']
coll = db1['test0']
coll.insert_one(d)
