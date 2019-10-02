from flask import Flask
from flask import request
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"
mongo = PyMongo(app)


@app.route('/show',methods=['GET'])
def start():
    data={}
    data=mongo.db.Adduser.find({})
    return dumps(data)


@app.route('/create', methods=['POST'])
def user_create():
    data = {}
    Adduser=[]
    doc_count=mongo.db.users.count_documents({})
    count=0
    if doc_count > 0:
        count=doc_count
    else:
        count=0
    for x in range(0,100):
        count=count+1
        data["_id"] = ObjectId()
        data["name"]=request.json["name"]+str(count)
        data["phone"]=request.json["phone"]+str(count)
        mongo.db.Adduser.insert(data)
    print(Adduser)
    return dumps("users added")

# @app.route('/show')
# def start():
#     data={}
#     data=mongo.db.library.find({})
#     return dumps(data)

# @app.route('/users/<int:user_id>', methods=['POST'])
# def user_id(_id):
#     name=request.json["name"]
#     mongo.db.library.update({"_id":_id},{"$push":{"children":{"name":name, "checked":"not read yet"}}})
#     return dumps({"message":"Book Added"})

@app.route('/create/blog', methods=['POST'])
def create_blog():
    data = {}
    blogs=[]
    doc_count=mongo.db.users.count_documents({})
    count=0
    if doc_count > 0:
        count=doc_count
    else:
        count=0
    for x in range(0,100):
        count=count+1
        data["_id"] = ObjectId()
        data["heading"]=request.json["heading"]+str(count)
        data["text"]=request.json["text"]+str(count)
        mongo.db.blogs.insert(data)
    print(blogs)
    return dumps("blogs added")

# @app.route('/blogs/<Object:user_id>/<Object:_id>', methods=['POST'])
# def add_comment(user_id,_id):
#     user_id=request.json["user_id"]
#     _id=request.json["_id"]
#     checked=["commented"]
#     mongo.db.library.update({"user_id":user_id},{"$push":{"children":{"name":name, "checked":"not read yet"}}})
#     return dumps({"message":"Book Added"})



@app.route("/creat/userblog/<int:user_id>/<int:item_index>",methods = ["POST"])
def creat_blog(user_id,item_index):
    data ={}
    item_index=item_index-1
    data["comment"] = request.json["comment"]
    mongo.db.blog.update({"$push":{"heading."+str(item_index)+".Comment":data}})
    return dumps(data)



