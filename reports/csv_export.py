import csv
from pathlib import Path


class CSVExporter:

    def export(self, keyword, rows):

        export_dir = Path("exports")
        export_dir.mkdir(exist_ok=True)

        filename = keyword.lower().strip()
        filename = filename.replace(" ", "_")
        filename = filename.replace("/", "_")
        filename = filename.replace("\\", "_")

        file_path = export_dir / f"{filename}_report.csv"

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Family",
                "Listings",
                "Total Sold",
                "Demand",
                "Competition",
                "Saturation",
                "Lowest Price",
                "Average Price",
                "Median Price",
                "Highest Price",
                "Market Segment",
                "Final Score",
                "Recommendation"
            ])

            for row in rows:

                writer.writerow([

                    row["family"],

                    row["listings"],

                    row["sold"],

                    row["demand"],

                    row["competition"],

                    row["saturation"],

                    row["lowest"],

                    row["average"],

                    row["median"],

                    row["highest"],

                    row["segment"],

                    row["score"],

                    row["decision"]

                ])

        return str(file_path)