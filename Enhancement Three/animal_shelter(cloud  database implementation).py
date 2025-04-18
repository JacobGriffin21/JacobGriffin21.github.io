from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """


    def __init__(self, database_name="AAC", collection_name="animals"):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        username = "jacobgriffin2133" # username for MONGODB Atlas cloud server
        password= "Tateisnice30-" # password for MONGODB Atlas cloud server
        cluster = "cs499cloudserver.b124vea.mongodb.net"  # Cluster name created in MONGODB Atlas
        dbname = database_name 
        
        # cluster string connection 
        uri = (f"mongodb+srv://{username}:{password}@{cluster}/{dbname}?retryWrites=true&w=majority")
        
        # Connection the MONGODB Atlas
        self.client = MongoClient(uri)
        self.database = self.client[dbname]
        self.collection = self.database['animals']
        print("Connection to database Successful") # For personal use to ensure I connected to the database


    # Complete this create method to implement the C in CRUD.
    # Added a boolean to express if the document is created successfully or not
    def create(self, data):
        # Raise an exception if data is None
        if data is None:
            raise Exception("Nothing to save, because data parameter is empty")
        
        # Insert the data into the database and get the ObjectId of the inserted document
        result = self.database.animals.insert_one(data)
        
        # Print statement added for debugging
        print("Creation Complete")
        
        # Return the inserted ObjectId
        return result.inserted_id
        

# Create Method to implement the R in CRUD
# Using a boolean to identify completion of the function
    def read(self, data):
        read_successfully = False
        results = [] # empty list to store the results of the read file

        if data is not None:
           results_cursor = self.database.animals.find(data) # using the find function to read the data
           
           results = [result for result in results_cursor] # dictionary form to be similar to JSON
           
           read_successfully = True
        else:
           raise Exception("Nothing to read, because data parameter is empty")
           
	# Print statement to ensure the function is completed (using for personal use and readability)
        if read_successfully:
           print("Read Complete")
           
           # Return the results of the document that is read
           return results

