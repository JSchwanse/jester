import os
import unittest
from os.path import dirname

from j_core import Runtime as Runtime_Module
from j_core.Runtime import Runtime
from j_core.businessobject.BusinessObject import Base
from j_core.businessobject.businessobject_decorator import Registry
from j_core.config import DatabaseConfiguration

__all__ = ['DatabaseTestCases']


class DatabaseTestCases:
    @staticmethod
    def get_db_config_path() -> str:
        # find db config file regardless from where the test is started
        # the config file must reside at the top-level of the 'tests' folder, e.g.: '.../tests/test-db-config.xml'
        db_config_dir_name = 'tests'
        test_db_config_filename = 'test-db-config.xml'
        current_path = os.getcwd()
        if os.path.isfile(f'{current_path}/{db_config_dir_name}/{test_db_config_filename}'):
            # default case: test executed in root, which should be the parent of the 'tests'-folder
            return f'{current_path}/{db_config_dir_name}/{test_db_config_filename}'

        while not current_path.endswith(db_config_dir_name):
            current_path = dirname(current_path)  # climb up
        return f'{current_path}/{test_db_config_filename}'

    class BaseDatabaseTest(unittest.TestCase):
        def __init__(self, method_name: str = 'runTest'):
            # make db connection
            # db_config = DatabaseConfiguration('./../test-db-config.xml')
            db_config = DatabaseConfiguration(DatabaseTestCases.get_db_config_path())
            db_connection = db_config.get_connection('test')
            if db_connection is not None:
                Runtime_Module.initialize(db_connection)

            # continue with unittest constructor
            super().__init__(method_name)

        def setUp(self) -> None:
            from jester.Testdata import Testdata

            # reset all tables
            for table in reversed(Base.metadata.sorted_tables):
                session = Runtime.Session()
                session.execute(table.delete())
                session.commit()

            # insert test data
            data = Testdata.get(self)
            session = Runtime.Session()
            for bo in data:
                # resolve business object
                bo_class = Registry.get(bo)
                if bo_class is None:
                    continue

                for entry in data[bo]:
                    bo_inst = bo_class(**entry)
                    session.add(bo_inst)

            session.commit()
