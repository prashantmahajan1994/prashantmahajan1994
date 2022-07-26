import pymongo
client = pymongo.MongoClient("mongodb+srv://pmahajan:mXqIHVJZ0p5FkM6W@cluster0.albf6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

a={
    "name" : "prashant",
    "email.id" : "m.prashantmahajan@gmail.com",
    "password" : "India@2022"
}
db1=client["mongotest"]
coll=db1['test']
coll.insert_one(a)

x="prashant"
for i in range(len(x)):
    print (i)

