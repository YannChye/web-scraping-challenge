from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create an instance of Flask
app=Flask(__name__)

#  establish Mongo connection
mongo=PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# root route
@app.route("/")
def home():
    marsdata = mongo.db.collection.find_one()
    return render_template("index.html", mars=marsdata)

# scrape route
@app.route("/scrape")
def scrape():
    mars_data=scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)