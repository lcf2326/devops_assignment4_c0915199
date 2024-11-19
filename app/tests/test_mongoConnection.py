import os
import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''
Testing mongodb connection using ping command. After connection is established the test is passed.
If not, the test fails and gives a "Connection failed" message. 
After the test is done, the connection is closed for further use.
'''

class TestMongoDBConnection(unittest.TestCase):
    # setting up the connection
    def setUp(self):
        mongo_uri = os.getenv('MONGODB_URI')
        self.client = MongoClient(mongo_uri)

    def test_mongo_connection(self):
        # ping to the mongo db server
        try:
            self.client.admin.command("ping")
            connected = True
        except ConnectionFailure:
            connected = False

        # assert the connection, with "Connection failed" message if connection is false
        self.assertTrue(connected, "Connection failed")

    def tearDown(self):
        # Close the connection after the test is done
        self.client.close()

if __name__ == "__main__":
    unittest.main()
