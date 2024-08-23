from typing import Callable


class Assertions:
    @staticmethod
    def assertAnyInList[T](_list: list[T], element_checker: Callable[[T], bool]):
        any_match = False
        for element in _list:
            if element_checker(element) is True:
                any_match = True
                break

        assert any_match is True

    @staticmethod
    def assertAllinList(_list: list, element_checker):
        all_match = True
        for element in _list:
            if element_checker(element) is False:
                all_match = False
                break

        assert all_match is True
