from pymongo import MongoClient

#from flask import Flask, render_template, request, jsonify, redirect,url_for,session
uri = "mongodb+srv://sampleR:sampleR@cluster0.ljwn3ub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client["stock"]
#collection = db["admin"]


# Select the collection
pdt = db['product']

# Update the document
#print(col.find({'_id': 1}))
# Close the connection

product_id = 3
n_stock = 33
new_stock = str(n_stock)
pdt.update_one({'_id': product_id}, {'$set': {'stock': new_stock}})
product = pdt.find_one({'_id': product_id})
if product:
    print( 'Success', "True" , 'remainingStock',product['stock'])
else:
    print('success', "False" , 'error', 'Product not found')
client.close()
