import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://dhananjayg4:ddg1992@cluster92.t8e4svk.mongodb.net/?retryWrites=true&w=majority"
)
db = client.test

data = {
    "Name": "Dhananjay",
    "Surname": "Gavale",
    "Email-id": "dhannanjayg4@gmail.com",
    "Subject": ["DSA", "FSDS" , "Excel"]
}

database = client['Myinfo']
collection = database["Dhanu"]
collection.insert_one(data)
