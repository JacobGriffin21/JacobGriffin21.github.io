import unittest
from pymongo import MongoClient
from bson.objectid import ObjectId
from animal_shelter import AnimalShelter

class TestAnimalShelter(unittest.TestCase):
    
    # Setting up the class for the unitTest
    @classmethod
    def setUpClass(cls):
        cls.shelter = AnimalShelter(database_name="TestAAC", collection_name="test animals")
        # This ensures you're using TestACC and the 'test animals' collection
        print("Connected to TestAAC database for testing.")
    
    # Setsup a new instance of AnimalShelter before each test
    def setUp(self):
        # Create a new instance of AnimalShelter for each test case
        self.shelter = AnimalShelter(database_name="TestAAC", collection_name="test animals")
        self.insert_id = self.shelter.create({"name": "Test Animal"})d
        self.assertIsNotNone(self.insert_id)
    
    # Tears down the database before each test so the new data can be inserted
    def tearDown(self):
        self.shelter.client.close()
    
    # Testing the create function for a new animal
    def test_create(self):
        test_animal = {"name": "Jacob", "breed": "Labrador", "age": 3} # Animal properties that are being created
        result = self.shelter.create(test_animal)
        self.assertIsInstance(result, ObjectId)
        
        inserted = self.shelter.collection.find_one({"name": "Jacob"}) # Find the data that was inserted
        self.assertIsNotNone(inserted)
    
    # Testing the read function of an animal already in the database
    def test_read(self):
        test_animal = {"name": "Dallas", "breed": "Newfoundland", "age" : 3} # Data that is going to be read from the database
        self.shelter.collection.insert_one(test_animal)
        
        results = self.shelter.read({"name": "Dallas"}) # Read the following properties from the database
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]["breed"], "Newfoundland")
    
    # This is for reading an empty result
    def test_read_empty(self):
        results = self.shelter.read({"name":"No Name"})
        self.assertEqual(len(results), 0)
    
    # This is for throwing an exception if an instance is trying to be created but no values are inserted 
    def test_create_empty_data(self):
        with self.assertRaises(Exception): # Throw the exception 
            self.shelter.create(None)
    
# Makes sure all test cases are being ran 
if __name__ == '__main__':
    unittest.main()

        


