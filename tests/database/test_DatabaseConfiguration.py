import unittest

from j_core.config.database_config import DatabaseConfiguration

from jester.DatabaseTestCases import DatabaseTestCases


class DatabaseConfigurationTest(unittest.TestCase):
    def test_read_config_file(self):
        # test_config_file_path = './../test-db-config.xml'
        test_config_file_path = DatabaseTestCases.get_db_config_path()
        database_config = DatabaseConfiguration(test_config_file_path)

        self.assertEqual(test_config_file_path, database_config.config_path)
        self.assertEqual(1, len(database_config.connections))
        self.assertIsNotNone(database_config.get_connection('shogi'))

        self.assertEqual('postgres', database_config.get_connection('shogi').get_user())
        self.assertEqual('postgres', database_config.get_connection('shogi').get_password())
        self.assertEqual('localhost', database_config.get_connection('shogi').get_host())
        self.assertEqual('5432', database_config.get_connection('shogi').get_port())
        self.assertEqual('shogitestdb', database_config.get_connection('shogi').get_database())
        # self.assertEqual('psycopg2', database_config.get_connection('shogi').get_dialect())
        self.assertEqual('public', database_config.get_connection('shogi').get_schema())
        self.assertEqual('postgresql', database_config.get_connection('shogi').get_driver())
        self.assertEqual('postgresql+psycopg2://postgres:postgres@localhost:5432/shogitestdb',
                         database_config.get_connection('shogi').get_connection_string())


if __name__ == '__main__':
    unittest.main()
