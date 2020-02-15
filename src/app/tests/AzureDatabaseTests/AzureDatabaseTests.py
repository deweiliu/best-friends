from app.database.azure_database import AzureDatabase
import random

import unittest
class AzureDatabaseTests(unittest.TestCase):


    def testDrop(self):
        AzureDatabase.drop('Persondewei')

    def testCreate(self):
        result = AzureDatabase.create('TableVS11','ID INTEGER PRIMARY KEY','Hi_name VARCHAR(100)')



