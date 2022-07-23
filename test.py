import pymongo
client = pymongo.MongoClient("mongodb+srv://ujjwall:Ujjwal2609@cluster0.3y5ya.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"Ujjwal",
    "mail_id" : "ujjwalrajput3107@gmail.com",
    "surname": "rajput"
}
d={
    "name":"Ujjwal",
    "mail_id" : "ujjwalrajput3107@gmail.com",
    "surname": "rajput"
}
d={
    "name":"Ujjwal",
    "mail_id" : "ujjwalrajput3107@gmail.com",
    "surname": "rajput"
}
d={
    "name":"Ujjwal",
    "mail_id" : "ujjwalrajput3107@gmail.com",
    "surname": "rajput"
}
db1=client["mongotest"]
coll=db1['test']
coll.insert_one(d)


