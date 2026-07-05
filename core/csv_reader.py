from pathlib import Path
import pandas as pd


class CSVReader:
    """
    Read CSV or Excel files.
    """

    @staticmethod
    def read(file_path: str):

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        suffix = path.suffix.lower()

        if suffix == ".csv":
            return pd.read_csv(path)

        elif suffix in [".xlsx", ".xls"]:
            return pd.read_excel(path)

        else:
            raise ValueError("Unsupported file format.")