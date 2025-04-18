from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
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
        USER = 'aacuser'
        PASS = 'griffin8'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32012
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection to database Successful") # For personal use to ensure I connected to the database


# Complete this create method to implement the C in CRUD.
# Added a boolean to express if the document is created successfully or not
    def create(self, data): 
        
        # Boolean created to identify completion of the function w/False and True
        created_successfully = False
        if data is not None:
            self.database.animals.insert_one(data) # data needs to be in dictionary form to be similar to JSON
            created_successfully = True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
        # Print statement added so I can ensure the function runs completely through
        if (created_successfully):
            print("Creation Complete")
            
        return created_successfully
        

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

