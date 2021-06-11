import unittest
from object_manager import object_manager


class PdwUtilsTest(unittest.TestCase):
    def setUp(self):
        self.objm = object_manager("fortesting")
        self.objm.object_reset()


    def test_object_create(self):
        self.objm.object_create()
        res = self.objm.object_list()
        self.assertEqual(1 in res, True, "Its present")
        self.objm.object_create()
        res = self.objm.object_list()
        self.assertEqual(len(res), 2, "Its present")

    def test_object_get(self):
        self.objm.object_create()
        self.objm.object_create()
        self.objm.object_create()
        theobj = self.objm.object_get()
        res = self.objm.object_list()
        self.assertEqual(theobj not in res, True, "Its not present")

    def test_object_free(self):
        self.objm.object_create()
        self.objm.object_create()
        self.objm.object_create()
        theobj = self.objm.object_get()
        res = self.objm.object_list()
        self.assertEqual(theobj not in res, True, "Its not present")
        self.objm.object_free(theobj)
        res = self.objm.object_list()
        self.assertEqual(theobj in res, True, "Its present")


    def tearDown(self):
        self.objm.delete_data_file()

if __name__ == '__main__':
    unittest.main()
