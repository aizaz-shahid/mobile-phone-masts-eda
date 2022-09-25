from pprint import pprint

from src.analysis import (
    get_first_n_rows,
    get_masts_grouped_by_tenant_name,
    get_masts_with_25_years_lease,
    get_masts_with_lease_start_date_between_dates,
    get_total_rent_for_masts_with_25_years_lease,
)
from src.constants import FILE_PATH, CSVColumns
from src.file import FileReader
from src.helpers import sort_data_by_key


def print_options() -> None:
    print("1. Get first n rows")
    print("2. Get list of mast data with 'Lease Years' = 25, and their total rent")
    print("3. Get total rent for masts with 25 years lease")
    print("4. Get masts data grouped by 'Tenant Name'")
    print(
        "5. Get data for rentals with 'Lease Start Date' between 1st June 1999 and 31st August 2007"
    )
    print("6. Exit")


if __name__ == "__main__":
    reader = FileReader(
        file_path=FILE_PATH,
        data_types={
            CSVColumns.CURRENT_RENT: "float",
            CSVColumns.LEASE_START_DATE: "datetime",
            CSVColumns.LEASE_END_DATE: "datetime",
            CSVColumns.LEASE_YEARS: "int",
        },
    )
    data = reader.read_csv()
    sort_data_by_key(data=data, key=CSVColumns.CURRENT_RENT)
    options = {
        "1": get_first_n_rows,
        "2": get_masts_with_25_years_lease,
        "3": get_total_rent_for_masts_with_25_years_lease,
        "4": get_masts_grouped_by_tenant_name,
        "5": get_masts_with_lease_start_date_between_dates,
    }
    while True:
        print_options()
        choice = input("Enter your choice: ")
        if choice == "6":
            break
        try:
            pprint(options[choice](data))
        except KeyError:
            print("Invalid option")
