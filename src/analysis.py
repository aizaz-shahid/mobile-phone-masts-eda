from datetime import datetime
from pprint import pprint
from typing import Any

from src.constants import CSVColumns
from src.helpers import group_by_key


def get_first_n_rows(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    n = int(input("Enter n: "))
    return data[:n]


def get_masts_with_25_years_lease(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    masts_with_25_years_lease = [
        mast for mast in data if mast[CSVColumns.LEASE_YEARS] == 25
    ]
    pprint("Properties with 25 years lease are: ")
    return masts_with_25_years_lease


def get_total_rent_for_masts_with_25_years_lease(data: list[dict[str, Any]]) -> int:
    masts_with_25_years_lease = [
        mast for mast in data if mast[CSVColumns.LEASE_YEARS] == 25
    ]
    total_rent = sum(
        [mast[CSVColumns.CURRENT_RENT] for mast in masts_with_25_years_lease]
    )
    pprint(f"The total rent for masts with 25 years lease is: ")
    return total_rent


def get_masts_grouped_by_tenant_name(data: list[dict[str, Any]]) -> dict[str, int]:
    grouped_by_tenant_name = group_by_key(data, key=CSVColumns.TENANT_NAME)
    pprint("Masts data grouped by 'Tenant Name': ")
    return {tenant: count for tenant, count in grouped_by_tenant_name.items()}


def get_masts_with_lease_start_date_between_dates(
    data: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    start_date = datetime.strptime("1 June 1999", "%d %B %Y")
    end_date = datetime.strptime("31 August 2007", "%d %B %Y")
    masts_with_lease_start_date_between_dates = [
        mast
        for mast in data
        if start_date
        <= datetime.strptime(mast[CSVColumns.LEASE_START_DATE], "%d/%m/%Y")
        <= end_date
    ]
    pprint(
        f"The data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007 is: "
    )
    return masts_with_lease_start_date_between_dates
