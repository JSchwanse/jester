import unittest

from j_core.config.database_config import DatabaseConfiguration
from jester.DatabaseTestCases import DatabaseTestCases


class DatabaseConfigurationTest(unittest.TestCase):
    def test_read_config_file(self):
        # test_config_file_path = './../test-db-config.xml'
        test_config_file_path = DatabaseTestCases.get_db_config_path()
        database_config = DatabaseConfiguration(test_config_file_path)
        test_connection_alias = 'test'

        self.assertEqual(test_config_file_path, database_config.config_path)
        self.assertEqual(1, len(database_config.connections))
        self.assertIsNotNone(database_config.get_connection(test_connection_alias))

        self.assertEqual('postgres', database_config.get_connection(test_connection_alias).get_user())
        self.assertEqual('postgres', database_config.get_connection(test_connection_alias).get_password())
        self.assertEqual('localhost', database_config.get_connection(test_connection_alias).get_host())
        self.assertEqual('5432', database_config.get_connection(test_connection_alias).get_port())
        self.assertEqual('testdb', database_config.get_connection(test_connection_alias).get_database())
        self.assertEqual('psycopg2', database_config.get_connection(test_connection_alias).get_dialect())
        self.assertEqual('public', database_config.get_connection(test_connection_alias).get_schema())
        self.assertEqual('postgresql', database_config.get_connection(test_connection_alias).get_driver())
        self.assertEqual('postgresql+psycopg2://postgres:postgres@localhost:5432/testdb',
                         database_config.get_connection(test_connection_alias).get_connection_string())


if __name__ == '__main__':
    unittest.main()
