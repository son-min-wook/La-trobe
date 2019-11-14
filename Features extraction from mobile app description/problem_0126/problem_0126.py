from pymongo import MongoClient

client = MongoClient()
db = client.googleapp  # use a database called "test_database"
collection = db.features   # and inside that DB, a collection called "files"

f = open('result.txt',encoding='UTF-16')  # open a file
text = f.read()    # read the entire contents, should be UTF-8 text

# build a document to be inserted
text_file_doc = {"file_name": "result.txt", "contents" : text }
# insert the contents into the "file" collection
collection.insert(text_file_doc)