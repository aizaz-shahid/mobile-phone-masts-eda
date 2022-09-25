from src import analysis
from src.analysis import (
    get_first_n_rows,
    get_masts_grouped_by_tenant_name,
    get_masts_with_25_years_lease,
    get_masts_with_lease_start_date_between_dates,
    get_total_rent_for_masts_with_25_years_lease,
)


def test_get_first_n_rows():
    data = [
        {"Lease Start Date": "01/06/1999", "Current Rent": 100},
        {"Lease Start Date": "01/05/2005", "Current Rent": 200},
        {"Lease Start Date": "31/08/2010", "Current Rent": 300},
    ]
    expected = [
        {"Lease Start Date": "01/06/1999", "Current Rent": 100},
        {"Lease Start Date": "01/05/2005", "Current Rent": 200},
    ]
    analysis.input = lambda _: "2"
    actual = get_first_n_rows(data)
    assert actual == expected


def test_get_masts_with_25_years_lease():
    data = [
        {"Lease Years": 23, "Current Rent": 100},
        {"Lease Years": 25, "Current Rent": 200},
        {"Lease Years": 24, "Current Rent": 300},
    ]
    expected = [{"Lease Years": 25, "Current Rent": 200}]
    actual = get_masts_with_25_years_lease(data)
    assert actual == expected


def test_get_total_rent_for_masts_with_25_years_lease():
    data = [
        {"Lease Years": 25, "Current Rent": 100},
        {"Lease Years": 23, "Current Rent": 200},
        {"Lease Years": 25, "Current Rent": 300},
    ]
    expected = 400
    actual = get_total_rent_for_masts_with_25_years_lease(data)
    assert actual == expected


def test_get_masts_grouped_by_tenant_name():
    data = [
        {"Tenant Name": "A", "Current Rent": 100},
        {"Tenant Name": "A", "Current Rent": 200},
        {"Tenant Name": "B", "Current Rent": 300},
    ]
    expected = {"A": 2, "B": 1}
    actual = get_masts_grouped_by_tenant_name(data)
    assert actual == expected


def test_get_masts_with_lease_start_date_between_dates():
    data = [
        {"Lease Start Date": "01/06/1999", "Current Rent": 100},
        {"Lease Start Date": "01/05/2005", "Current Rent": 200},
        {"Lease Start Date": "31/08/2010", "Current Rent": 300},
    ]
    expected = [
        {"Lease Start Date": "01/06/1999", "Current Rent": 100},
        {"Lease Start Date": "01/05/2005", "Current Rent": 200},
    ]
    actual = get_masts_with_lease_start_date_between_dates(data)
    assert actual == expected
