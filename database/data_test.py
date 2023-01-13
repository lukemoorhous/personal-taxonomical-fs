import unittest
from data import DTO, ContentFile, ContentVersion


class DTO_Test(unittest.TestCase):

    def test_init(self):
        result = DTO(123)
        self.assertEqual(result.id, 123)

    def test_emptyInit(self):
        result = DTO()
        self.assertEqual(result.id, None)

    def test_eq(self):
        obj = DTO(123)
        other = DTO('123')
        result = obj.__eq__(other)
        self.assertFalse(result)


class ContentFile_Test(unittest.TestCase):

    def test_init(self):
        result = ContentFile(id=929, filename='kek', filetype='bin')
        self.assertEqual(result.id, 929)
        self.assertEqual(result.filename, 'kek')
        self.assertEqual(result.fileextension, None)

    def test_eq(self):
        file = ContentFile(id=929, filename='kek', filetype='bin')
        other = ContentFile(id=929, filename='kek', filetype='bin')

        self.assertTrue(file.__eq__(other))

    def test_eq_differentIdSameValues(self):
        file = ContentFile(filename='kek', filetype='bin')
        other = ContentFile(id=929, filename='kek', filetype='bin')

        self.assertFalse(file.__eq__(other))

    def test_eq_sameIdDifferentValues(self):
        file = ContentFile(
            id=929, filename='keksimus maximus', fileextension='.jpg')
        other = ContentFile(id=929, filename='kek', filetype='bin')

        self.assertFalse(file.__eq__(other))


class ContentVersion_Test(unittest.TestCase):

    def test_init(self):
        file = ContentFile(
            id=929, filename='keksimus maximus', fileextension='.jpg')
        result = ContentVersion(content_file=file)

        self.assertEqual(None, result.id)
        self.assertEqual(929, result.content_file.id)

    def test_eq(self):
        content = ContentVersion(version='1', name='kek')
        other = ContentVersion(version='1', name='kek')

        self.assertTrue(content.__eq__(other))

    def test_eq_versionChanged(self):
        file = ContentFile(
            id=929, filename='keksimus maximus', fileextension='.jpg')
        version1 = ContentVersion(version='1', content_file=file)
        version2 = ContentVersion(version='2', content_file=file)

        self.assertFalse(version1.__eq__(version2))
        self.assertTrue(version1.content_file.__eq__(version2.content_file))


if __name__ == '__main__':
    unittest.main()
