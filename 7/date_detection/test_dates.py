from date_detection import normalize_date, check_date


def test_normalize_date():
    assert normalize_date(45, 12, 2020) == "45/12/2020"
    assert normalize_date(5, 12, 2020) == "05/12/2020"
    assert normalize_date(31, 2, 2020) == "31/02/2020"
    assert normalize_date(31, 4, 2021) == "31/04/2021"
    

def test_check_date():
    assert check_date(20, 10, 2003)
    assert check_date(1, 10, 3)
    assert check_date(31, 10, 2000)
    assert check_date(29, 2, 2000)
    assert not check_date(29, 2, 1999)
    assert not check_date(31, 11, 2000)
    assert not check_date(31, 4, 2000)
    assert not check_date(31, 6, 2000)



    # Assume that the days range from 01 to 31, the months range
    # from 01 to 12, and the years range from 1000 to 2999
