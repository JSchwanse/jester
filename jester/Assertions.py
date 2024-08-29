from typing import Callable, TypeVar

__all__ = ['Assertions']

T = TypeVar('T')


class Assertions:
    @staticmethod
    def assertAnyInList(_list: list[T], element_checker: Callable[[T], bool]) -> None:
        any_match = any(element_checker(element) for element in _list)
        assert any_match

    @staticmethod
    def assertAllinList(_list: list[T], element_checker: Callable[[T], bool]) -> None:
        all_match = all(element_checker(element) is not False for element in _list)
        assert all_match
