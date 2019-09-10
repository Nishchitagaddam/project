from flask import Flask
import pymongo

client = pymongo.MongoClient()
db = client.StudentData

app = Flask(__name__)

@app.route('/')
def insert():
    user_collection = db.Students
    user_collection.insert({"name": "Cloud", "age": 12})
    #user_collection.insert({"name": "Bob", "age": 15})

    return '<h1> Added a Student<h1>'

@app.route('/find')
def read():
    user_collection = db.Students
    user = user_collection.find_one({"name": "Cloud"})
    name = user['name']
    age = user['age']

    data = {'name':name, 'age': age}
    
    # return ' {% for key, value in user.iteritems() %} <tr><th > {{ key }} </th> <td> {{ value }} </td> </tr> {% endfor %}'

    # return f"Student {data}."
    return data

@app.route('/update')
def update():
     user_collection = db.Students
     user = user_collection.find_one({"name": "Cloud"})
     user["age"] = 14
     user_collection.save(user)
     return '<h1> Updated user<h1>'

@app.route('/delete')
def delete():
     user_collection = db.Students
     user = user_collection.find_one({"name": "Cloud"})
     #user = user_collection.find_one({"name": "Bob"})
     user_collection.remove(user)
     return '<h1> Deleted user <h1>'


if __name__=="__main__":
    app.run()