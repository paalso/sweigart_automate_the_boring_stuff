from detect_dates import normalize_date


def test_normalize_date():
    assert normalize_date(45, 12, 2020) == "45/12/2020"
    assert normalize_date(5, 12, 2020) == "05/12/2020"
    assert normalize_date(31, 2, 2020) == "31/02/2020"
    assert normalize_date(31, 4, 2021) == "31/04/2021"

    # Assume that the days range from 01 to 31, the months range
    # from 01 to 12, and the years range from 1000 to 2999
