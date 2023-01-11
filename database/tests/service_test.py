import unittest
from service import DATABASE
from data import ContentFile, ContentVersion


class DATABASE_test(unittest.TestCase):

    def test_init(self):
        self.assertNotEqual(None, DATABASE.location)
    
    def test_tablesCreated(self):
        tables = DATABASE.__database_tables__(DATABASE.connection().cursor())
        
        self.assertTrue(tables.__contains__(ContentFile.__name__))
        self.assertTrue(tables.__contains__(ContentVersion.__name__))
    
    def test_insertContentFile(self):
        cFiles = [ContentFile(filename='kek')]
        
        result = DATABASE.insert(cFiles)
        print(result)