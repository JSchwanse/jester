import os.path
import pathlib
import unittest

from jester.DatabaseTestCases import DatabaseTestCases


class DatabaseTestCasesTest(unittest.TestCase):
    def test_db_config_path_resolution(self):
        # read the db config path and check its correctness
        # Because a path can be specified with slashes or backslashes, we need to compare the resolved normpath
        resolved_db_config_file_path = pathlib.Path(DatabaseTestCases.get_db_config_path()).resolve()
        resolved_file_path_from_file = pathlib.Path(
            os.path.dirname(os.path.abspath(__file__)) + '/../test-db-config.xml').resolve()
        self.assertEqual(os.path.normcase(resolved_file_path_from_file), os.path.normcase(resolved_db_config_file_path))


if __name__ == '__main__':
    unittest.main()
