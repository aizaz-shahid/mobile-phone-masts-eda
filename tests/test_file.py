from src.file import FileReader


class TestFileReader:
    def test_read_csv(self):
        data = FileReader(file_path="tests/data/test.csv").read_csv()
        expected = [{"id": "1", "name": "John", "dob": "20 May 1997", "age": "23"}]
        assert data == expected

    def test_read_csv_with_type_casting(self):
        data = FileReader(
            file_path="tests/data/test.csv",
            data_types={"id": "int", "age": "int", "dob": "datetime"},
        ).read_csv()
        expected = [{"id": 1, "name": "John", "dob": "20/05/1997", "age": 23}]
        assert data == expected
