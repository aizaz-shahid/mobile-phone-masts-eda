# mobile-phone-masts-eda

### Description:
This is a data analysis and processing of mobile phone masts in the UK.
### Installation:
- Clone the repository
- Go to the root of the project using `cd mobile-phone-masts-eda`
- Create a virtual environment using `pyenv virtualenv 3.10.2 mobile-phone-masts-eda`
- Activate the virtual environment using `pyenv activate mobile-phone-masts-eda`
- Install the requirements using `pip install -r requirements.txt`
### Usage:
- Run the program using `python3 src/main.py`
- Run tests using `pytest tests`
    #### Options:
     1. Get first n rows
     2. Get list of mast data with 'Lease Years' = 25, and their total rent
     3. Get masts data grouped by 'Tenant Name'
     4. Get data for rentals with 'Lease Start Date' between 1st June 1999 and 31st August 2007
     5. Exit
### Data:
The data used for this EDA is in `data/` directory. The data is in `csv` format and contains the following columns:
- `Property Name`: Name of the property
- `Property Address[1]`: Address line 1 of the property
- `Property Address[2]`: Address line 2 of the property
- `Property Address[3]`: Address line 3 of the property
- `Property Address[4]`: Address line 4 of the property
- `Unit Name`: Name of the unit
- `Tenant Name`: Name of the tenant
- `Lease Start Date`: Start date of the lease
- `Lease End Date`: End date of the lease
- `Lease Years`: Number of years of the lease
- `Current Rent`: Current rent of the property
