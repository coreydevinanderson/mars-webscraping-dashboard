from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db


# Set Index
@app.route('/')
def index():
    mars_stuff = list(db.mars.find())[0]
    print(mars_stuff)

    return render_template('index.html', mars_stuff = mars_stuff)

@app.route('/scraper')
def scrape():

    # Run the scraper...
    mars_data = scrape_mars.scrape()
    mongo.db.mars.update({}, mars_data, upsert = True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)