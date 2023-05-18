from pprint import pprint

from compare_for_testing import CompareJson


class DiffError(AssertionError):
    def __init__(self, diff, message=''):
        pprint(diff)
        super().__init__(message or 'Данные не сошлись')


def compare(standard_data, response_data, accuracy=3, exclude_fields=()):
    difference = CompareJson(
        accuracy=accuracy,
        exclude_fields=exclude_fields,
        format_number=True,
        use_delta_for_checksum=True,
    )

    if result := difference(standard_data, response_data):
        raise DiffError(diff=result)
