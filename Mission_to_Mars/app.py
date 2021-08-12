
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn_url= "mongodb://localhost:27017"
mongo = pymongo.MongoClient(conn_url)


@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_data= mongo.mars_db.mars.find_one()
    print(mars_data)

    return render_template('index.html', listings=mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    result = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.mars_db.mars.update({}, result, upsert = True)

    # return redirect
    #return redirect("/", code=302)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
