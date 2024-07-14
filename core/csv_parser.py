import sys
from pathlib import Path

import pandas as pd


def combine_files_to_excel(input_files, output_file):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for file in input_files:
            file_ext = Path(file).suffix.lower()

            if file_ext == '.csv':
                df = pd.read_csv(file)
            elif file_ext == '.txt':
                df = pd.read_csv(file, delimiter='\t')
            else:
                continue

            sheet_name = Path(file).stem
            df.to_excel(writer, sheet_name=sheet_name, index=False)


def get_files():
    files = []

    for file in Path("utils").glob("**/*.csv"):
        files.append(str(file))
    return files
