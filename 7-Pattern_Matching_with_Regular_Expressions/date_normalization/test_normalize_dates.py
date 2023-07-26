from dates_normalizer import normalize_date, check_date


def test_normalize_date():
    assert normalize_date('2022-31-1') == '01/31/2022'
    assert normalize_date('01-11-1999') == '01/11/1999'
    assert normalize_date('01-1-1999') == '01/01/1999'
    assert normalize_date('1-01-1999') == '01/01/1999'
    assert normalize_date('1999/30/2') == '02/30/1999'
    assert normalize_date('25/12/2050') == '25/12/2050'
    assert normalize_date('32/01/1524') == '32/01/1524'


def test_check_date():
    assert check_date('11/30/2020')


test_normalize_date()
