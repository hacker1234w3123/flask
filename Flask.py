from flask import Flask,jsonify,request

app = Flask(__name__)


Contact = [
{'Contact':9987644456,'name':"Raju" ,'done': False,'id':1},
{'Contact':9876543222,'name':"Rahul" ,'done': False,'id':2}
]

# Get method
@app.route("/")
def getTask():
    return jsonify({'data':Contact})


#Post method
@app.route("/add_tasks",methods = ["POST"])
def addTasks():
    task = {'name':Contact[-1]['name']+1 , 
    'name':request.json['name'] , 
    'id':request.json.get('id',''),
    'done':False
    }
    Contact.append(task)
    return jsonify({"status":"error",'message':'Please provide the data!'})


# Run Function
if __name__ == '__main__':
    app.run(debug = True)
