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

    # def test_insertContentFile(self):
        # cFiles = [ContentFile(filename='kek')]
        # result = DATABASE.insert_ContentFiles(records=cFiles)

        # print(result)
    
    def test_insert(self):
        cFiles = [ContentFile(filename='kek')]
        DATABASE.insert(records=cFiles)
    
    def test_insert_multipleTypes(self):
        records = [ContentFile(filename='kek'), ContentVersion(name='notAFile')]

        caught = False;
        try:
            DATABASE.insert(records)
        except TypeError:
            caught = True
        
        self.assertTrue(caught)

if __name__ == '__main__':
    unittest.main()
