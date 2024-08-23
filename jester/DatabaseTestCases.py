import os
import unittest
from os.path import dirname

from j_core import Runtime as Runtime_Module
from j_core.Runtime import Runtime
from j_core.businessobject.BusinessObject import Base
from j_core.businessobject.businessobject_decorator import Registry
from j_core.config import DatabaseConfiguration

from jester.Testdata import Testdata


class DatabaseTestCases:
    @staticmethod
    def get_db_config_path():
        # find db config file regardless from where the test is started
        # the config file must reside at the top-level of the 'tests' folder, e.g.: '.../tests/test-db-config.xml'
        db_config_dir_name = 'tests'
        test_db_config_filename = 'test-db-config.xml'
        current_path = os.getcwd()
        while not current_path.endswith(db_config_dir_name):
            current_path = dirname(current_path)
        return f'{current_path}/{test_db_config_filename}'

    class BaseDatabaseTest(unittest.TestCase):
        def __init__(self, method_name='runTest'):
            # make db connection
            # db_config = DatabaseConfiguration('./../test-db-config.xml')
            db_config = DatabaseConfiguration(DatabaseTestCases.get_db_config_path())
            Runtime_Module.initialize(db_config.get_connection('shogi'))

            # continue with unittest constructor
            super().__init__(method_name)

        def setUp(self):
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
                for entry in data[bo]:
                    bo_inst = bo_class(**entry)
                    session.add(bo_inst)

            session.commit()
