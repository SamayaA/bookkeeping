import unittest

from bookkeeping import Bookkeeping

documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },
    {
        "type": "invoice",
        "number": "11-2", 
        "name": "Геннадий Покемонов"
     },
    {
        "type": "insurance", 
        "number": "10006", 
        "name": "Аристарх Павлов"
    }
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

class TestBookkeepingSystem(unittest.TestCase):
    def setUp(self):
        self.organization = Bookkeeping(directories, documents)

    def tearDown(self):
        del self.organization

    def test_find_document_owner(self):
        self.assertEqual(self.organization.find_document_owner("10006"), "Аристарх Павлов")

    def test_find_shelf(self):
        self.assertEqual(self.organization.find_shelf("11-2"), "1")
    
    def test_add_document(self):
        document = {
        "type": "id",
        "number": "300",
        "name": "David"
        }
        self.organization.add_document("300", "id", "David", '1')
        self.assertTrue(document == self.organization.documents[-1])
        self.assertTrue("300" in self.organization.directories['1'])
    
    def test_delete_document(self):
        self.organization.delete_document("300")
        document = {
        "type": "id",
        "number": "300",
        "name": "David"
        }
        self.assertTrue("300" not in self.organization.directories['1'])
        self.assertTrue(document not in self.organization.documents)

    def test_replace_document(self):
        self.organization.replace_document("11-2", "2")
        self.assertEqual(self.organization.find_shelf("11-2"), "2")

    def test_add_shelf(self):
        self.organization.add_shelf("5")
        self.assertTrue("5" in self.organization.directories.keys())
    

if __name__ == 'main':
    unittest.main()
    
