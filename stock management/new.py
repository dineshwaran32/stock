from flask import Flask, render_template
from pymongo import MongoClient


uri = "mongodb+srv://sampleR:sampleR@cluster0.ljwn3ub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client["stock"]
adm = db["product"]

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    # Retrieve products from MongoDB
    products = adm.find()

    return render_template('new.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
    
