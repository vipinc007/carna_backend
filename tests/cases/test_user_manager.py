import unittest
from DataManager.userManager import user_manager


class PdwUtilsTest(unittest.TestCase):
    def setUp(self):
        self.objm = user_manager("test.data")
        self.objm.reset()


    def test_create(self):
        ret = self.objm.create(None)
        self.assertEqual(ret["done"] == False, True)

        ret = self.objm.create({})
        self.assertEqual(ret["done"] == False, True)

        ret = self.objm.create({"email":None})
        self.assertEqual(ret["done"] == False, True)

        ret = self.objm.create({"name":"vipin","email":"test@gmail.com","country":"india"})
        self.assertEqual(ret["done"] ==True, True)

        res = self.objm.list()["data"]
        id_list= [int(r["id"]) for r in res]
        self.assertEqual(int(ret["id"]) in id_list, True)

        ret = self.objm.create({"name": "vipin", "email": "test@gmail.com", "country": "india"})
        self.assertEqual(ret["done"] == False, True, "Duplicate record check")

        ret1 = self.objm.create({"name":"mark","email":"mark@gmail.com","country":"usa"})
        res1 = self.objm.list()["data"]
        id_list = [int(r["id"]) for r in res1]
        self.assertEqual(int(ret1["id"]) in id_list, True, "Its present")



    def test_get(self):
        ret = self.objm.create({"name": "vipin", "email": "test@gmail.com", "country": "india"})
        res = self.objm.get(int(ret["id"]))["data"]
        self.assertEqual(int(ret["id"]) == int(res["id"]), True)

    def test_reset(self):
        ret = self.objm.create({"name": "vipin", "email": "test@gmail.com", "country": "india"})
        self.objm.reset()
        res = self.objm.list()["data"]
        self.assertEqual(len(res)==0, True)

    def test_edit(self):
        ret = self.objm.create({"name": "vipin", "email": "test@gmail.com", "country": "india"})
        ret2 = self.objm.edit(int(ret["id"]),{"name": "vipin 2", "email": "test@gmail.com", "country": "india"})
        res = self.objm.get(int(ret["id"]))["data"]
        self.assertEqual(res["name"]=="vipin 2", True)


    def tearDown(self):
        self.objm.delete_data_file()

if __name__ == '__main__':
    unittest.main()
