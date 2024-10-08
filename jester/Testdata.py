import importlib
from typing import Any

from jester.DatabaseTestCases import DatabaseTestCases

__all__ = ['Testdata']


class Testdata:
    data_path = 'data.data'

    @classmethod
    def get(cls, inst: DatabaseTestCases.BaseDatabaseTest) -> Any:
        module_path_parts = inst.__module__.split('.')
        module_name = module_path_parts.pop(len(module_path_parts) - 1)
        module_path = '.'.join(module_path_parts) + '.' if len(module_path_parts) > 0 else ''

        return getattr(importlib.import_module(module_path + cls.data_path, module_name), 'data')
