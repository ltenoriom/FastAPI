from pymongo import MongoClient

def test_mongodb_connection(uri):
    try:
        # Create a MongoClient instance
        client = MongoClient(uri)
        
        # Check if the connection is successful by accessing a database
        db = client.test_database
        collection = db.test_collection
        collection.insert_one({'test_key': 'test_value'})
        
        # If no exception is raised, the connection is successful
        print("MongoDB connection successful!")
        
        # Close the connection
        client.close()
    except Exception as e:
        print("Failed to connect to MongoDB:", e)

# Replace 'your_mongodb_uri' with your actual MongoDB URI
mongodb_uri = 'mongodb+srv://ltenorio:lolaso94@cluster0.yh8sri6.mongodb.net/'

# Test MongoDB connection
test_mongodb_connection(mongodb_uri)
