from enum import Enum


class Realm(Enum):
    PRODUCTION = ('production', 'prod')
    TEST = ('test', 'test-')
    ALON = ('test', 'test-alon-')

    def __init__(self, hadoop_database_name, elastic_index_prefix):
        self._hadoop_database_name = hadoop_database_name
        self._elastic_index_prefix = elastic_index_prefix

    @property
    def hadoop_database_name(self):
        return self._hadoop_database_name

    @property
    def elastic_index_prefix(self):
        return self._elastic_index_prefix
