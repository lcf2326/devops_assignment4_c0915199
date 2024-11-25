import pytest
import sys
import os

# Add the project root directory to sys.path so the test can find the 'app' module
# This is necessary to resolve ImportError when running tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask 'app' from the main application module
from app import app

# Define a pytest fixture to create a test client for Flask
@pytest.fixture
def client():
    """
    This fixture sets up the Flask test client, enabling us to send simulated
    HTTP requests to the application without running the server.
    """
    app.testing = True  # Set the app in testing mode to enable testing-related behavior
    # Use the app's test_client to simulate requests to the Flask app
    with app.test_client() as client:
        yield client  # Yield the test client to be used in the test function

def test_invalid_method(client):
    """
    This test checks that the application returns a 405 Method Not Allowed status
    when an invalid HTTP method (POST) is used on a route that only accepts GET requests.
    """
    # Simulate a POST request to the '/products' route, which is likely to accept only GET requests
    response = client.post('/products')
    
    # Assert that the response status code is 405, which indicates Method Not Allowed
    assert response.status_code == 405, "Expected status code 405 for invalid method"