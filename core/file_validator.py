from pathlib import Path


class FileValidator:

    @staticmethod
    def validate(file_path):

        path = Path(file_path)

        if not path.exists():
            return False

        if path.suffix.lower() not in [
            ".csv",
            ".xlsx",
            ".xls"
        ]:
            return False

        return True