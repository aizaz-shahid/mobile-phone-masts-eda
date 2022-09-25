from csv import DictReader
from datetime import datetime
from typing import Any

from src.helpers import get_full_file_path


class FileReader:
    def __init__(self, file_path: str, data_types: dict[str, str] | None = None):
        self.file_path = file_path
        self.data_types = data_types

    def read_csv(self) -> list[dict[str, Any]]:
        """
        Reads data from the file and returns it as a list of dictionaries
        """
        try:
            with open(get_full_file_path(self.file_path), "r") as file:
                reader = DictReader(file)
                return (
                    self._type_cast_data(data_stream=reader, data_types=self.data_types)
                    if self.data_types
                    else list(reader)
                )
        except FileNotFoundError:
            print(f"File not found at {self.file_path}")
            exit()

    @staticmethod
    def _type_cast_data(
        data_stream: DictReader, data_types: dict[str, str]
    ) -> list[dict[str, Any]]:
        """
        Applies type conversions to the data based on the data_types dictionary
        """
        transformed_data = []
        for row in data_stream:
            for col, type_ in data_types.items():
                try:
                    if type_ == "float":
                        row[col] = float(row[col])
                    elif type_ == "int":
                        row[col] = int(row[col])
                    elif type_ == "datetime":
                        row[col] = datetime.strptime(row[col], "%d %b %Y").strftime(
                            "%d/%m/%Y"
                        )
                except KeyError:
                    print(f"Column {col} not found in the file")
                    exit()
                except ValueError:
                    print(f"Invalid data type {type_} for column {col}")
                    exit()
            transformed_data.append(row)
        return transformed_data
