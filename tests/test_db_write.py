from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def test_mongodb_write():
    """
    This test verifies the ability to insert a document into MongoDB and 
    ensure it is properly inserted and retrievable.
    """
  # Fetch the MongoDB URI from the environment variables
    mongo_uri = os.getenv('MONGODB_URI')

    # Access the 'shop_db' database and 'products' collection
    db = client.shop_db
    collection = db.products

    # Define a test product to be inserted into the database
    test_product = {"name": "Test Product", "price": 100}

    # Insert the test document into the 'products' collection
    result = collection.insert_one(test_product)
    
    # Assert that the document was inserted successfully (inserted_id should not be None)
    assert result.inserted_id is not None, "Document insertion failed"

    # Retrieve the inserted document using its _id
    inserted_product = collection.find_one({"_id": result.inserted_id})

    # Assert that the inserted document was successfully retrieved
    assert inserted_product is not None, "Inserted document not found"
    
    # Verify the document's fields match the expected values
    assert inserted_product["name"] == "Test Product", "Product name does not match"
    assert inserted_product["price"] == 100, "Product price does not match"