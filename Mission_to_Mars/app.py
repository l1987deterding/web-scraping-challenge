from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn_url= "mongodb://localhost:27017"
mongo = pymongo.MongoClient(conn_url)


@app.route("/")
def index():
    mars_data = mongo.mars_db.mars.find_one()
    print(mars_data)

    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scrape():
    result = scrape_mars.scrape_info()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
