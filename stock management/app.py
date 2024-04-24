# app.py

from flask import Flask, render_template, request, jsonify, redirect,url_for,session
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__, template_folder="templates")

uri = "mongodb+srv://sampleR:sampleR@cluster0.ljwn3ub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["stock"]
adm = db["admin"]
pdt = db["product"] 
ti = db["time"]

@app.route("/")
def admi():
    products = pdt.find()

    return render_template("new.html", products=products)

@app.route("/login", methods=['POST', 'GET'])
def login():
    user = request.form['username']
    pas = request.form['password']
    for data in adm.find():
        if data["username"] == user:
            if data["password"] == pas:
                return render_template("index.html")
            elif data["username"] == user and data["password"] != pas:
                return render_template("login.html", info="Invalid Password")
            else:
                return render_template("login.html", info="Invalid Username")


@app.route("/add_product", methods=["POST"])
def add_product():
    if request.method == "POST":
        id = request.form["_id"]
        img = request.form["img"]
        title = request.form["title"]
        description = request.form["description"]
        stock = request.form["stock"]
        datetime = request.form["datetime"]
        product_data = {"_id":id,"img": img, "title": title, "description": description, "stock": stock, "datetime": datetime}
        pdt.insert_one(product_data)
        return redirect(url_for("index"))
    render_template("index.html")


@app.route('/home',methods=["POST"])
def index():
    return render_template('new.html')


@app.route("/login_page")
def login_page():
    return render_template("login.html")

@app.route('/update_datetime', methods=['POST'])
def update_datetime():
    data = request.json
    new_datetime = data.get('datetime')
    if new_datetime:
        ti.update_one({'_id': '1'}, {'$set': {'datetime_field': new_datetime}})
        return jsonify({'message': 'Datetime updated successfully'}), 200
    else:
        return jsonify({'error': 'Datetime not provided'}), 400


@app.route("/update_stock/<product_id>/<int:n_stock>", methods=["POST"])
def update_stock(product_id, n_stock):
    product_id = int(product_id)
    pdt.update_one({'_id': product_id}, {'$set': {'stock': n_stock}})
    product = pdt.find_one({'_id': product_id})
    print(product_id,n_stock)
    if product:
        return jsonify({'success': True, 'remainingStock': product['stock']})
    else:
        return jsonify({'success': False, 'error': 'Product not found'})

if __name__ == "__main__":
    app.run(debug=True)
