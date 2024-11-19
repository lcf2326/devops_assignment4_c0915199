import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Fetch the MongoDB URI from the environment variables
mongo_uri = os.getenv('MONGODB_URI')

# Initialize MongoDB client using the URI from the .env file
client = MongoClient(mongo_uri)
db = client.shop_db  # 'shop_db' is the database name in MongoDB Atlas
products_collection = db.products  # 'products' is the collection name in the database

@app.route('/')
@app.route('/home')
def home():
    """
    Home route that renders the home page.
    """
    return render_template('home.html')

@app.route('/products')
def products():
    """
    Products route that fetches product data from MongoDB and renders the products page.
    """
    # Fetch all products from the database
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5001)
