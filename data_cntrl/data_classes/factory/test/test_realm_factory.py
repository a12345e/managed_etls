import unittest
from data_cntrl.data_classes.model.realm import Realm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        realm: Realm = Realm.ALON
        assert realm.hadoop_database_name == Realm.ALON.hadoop_database_name
        assert realm.elastic_index_prefix == Realm.ALON.elastic_index_prefix


if __name__ == '__main__':
    unittest.main()
