"""
Excel Report Generator
"""

from pathlib import Path

import pandas as pd


class ExcelReport:

    def save(self, products):

        output = Path("data/output")

        output.mkdir(parents=True, exist_ok=True)

        file = output / "BD_Product_Intelligence_Report.xlsx"

        df = pd.DataFrame(products)

        with pd.ExcelWriter(file) as writer:

            df.to_excel(

                writer,

                index=False,

                sheet_name="Products"

            )

        return file