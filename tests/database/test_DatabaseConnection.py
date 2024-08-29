import unittest

from j_core import Runtime as Runtime_Module
from j_core.Runtime import Runtime
from j_core.config.database_config import DatabaseConfiguration
from jester.DatabaseTestCases import DatabaseTestCases


class DatabaseConnectionTest(unittest.TestCase):
    def test_db_connectivity(self):
        # test_config_file_path = './../test-db-config.xml'
        test_config_file_path = DatabaseTestCases.get_db_config_path()
        db_config = DatabaseConfiguration(test_config_file_path)
        Runtime_Module.initialize(db_config.get_connection('test'))

        self.assertIsNotNone(Runtime.Datasource)
        self.assertIsNotNone(Runtime.Session)


if __name__ == '__main__':
    unittest.main()
