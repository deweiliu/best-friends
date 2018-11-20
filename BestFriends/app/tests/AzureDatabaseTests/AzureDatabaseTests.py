from app.database.azure_database import AzureDatabase
import random

import unittest
class AzureDatabaseTests(unittest.TestCase):
    def testInsert(self):
        self.assertEqual(True,True)
        
        AzureDatabase.insert('TableVS11',str(random.randint(0,10000)),"'newname'","'newemai'")

    def testDrop(self):
        AzureDatabase.drop('Persondewei')

    def testSelect(self):
        result = AzureDatabase.select('*',"TableVS11")
        self.assertNotEqual(None,result)


    def testCreate(self):
        result = AzureDatabase.create('TableVS11','ID INTEGER PRIMARY KEY','Hi_name VARCHAR(100)')



