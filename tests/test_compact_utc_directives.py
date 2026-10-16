from datetime import datetime, timedelta, timezone

import pytest

from isodate.isodatetime import parse_datetime
from isodate.isostrf import strftime


@pytest.mark.parametrize("directive, suffix", [("%z", "+0200"), ("%h", "+02")])
@pytest.mark.parametrize("offset", [0, 2])
def test_compact_timezone_directives(directive, suffix, offset):
    value = datetime(2024, 7, 2, 6, 6, 2, tzinfo=timezone(timedelta(hours=offset)))

    actual = strftime(value, "%Y%m%dT%H%M%S" + directive)

    expected = "20240702T060602" + ("Z" if offset == 0 else suffix)
    assert actual == expected
    assert parse_datetime(actual) == value
