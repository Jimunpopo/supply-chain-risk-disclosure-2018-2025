# Reading and Verification Tools

These utilities use the Python standard library. Run them from the repository root with Python 3.

## Read a risk CSV

```bash
python 05_reading_tools/read_risk_csv.py 02_risk_disclosure_data/01_combined_panel/supply_chain_risk_panel_2018_2025.csv --rows 2
python 05_reading_tools/read_risk_csv.py 02_risk_disclosure_data/02_domain_data/supply_demand_risk_2018_2025.csv.zip --rows 2
```

The utility detects the header using `code`, `year`, and `denom`. It reads UTF-8 text with optional BOM, skips introductory notes, and returns values as strings. Empty cells remain empty strings. Company codes retain leading zeros.

For use in another Python script:

```python
import sys
from pathlib import Path

repository = Path.cwd()  # Run from the repository root.
sys.path.insert(0, str(repository / "05_reading_tools"))
from read_risk_csv import iter_risk_rows

path = repository / "02_risk_disclosure_data/02_domain_data/supply_demand_risk_2018_2025.csv.zip"
for row in iter_risk_rows(path):
    company_code = row["code"]
    accounting_year = int(row["year"])
    # Convert required numeric fields for the intended analysis.
```

## Verify file integrity

```bash
python 05_reading_tools/verify_files.py
```

The script compares current release sizes and SHA-256 digests with `04_data_verification/file_manifest.json`. It checks the nine data files and the original audit report, and verifies the CSV data-section hashes against those recorded for the originals. Original full-file hashes remain in separate `source_*` fields. The command does not require local copies of the originals.

## Read the financial workbook

Use `sheet1` in `03_financial_control_data/financial_control_variables.xlsx`. Row 1 contains field codes; rows 2 and 3 contain labels and units. Data begin on row 4. Exclude the two descriptive rows from the observations before matching, and preserve company codes as six-digit strings.

These tools read and verify the release files. They do not merge controls or estimate models.

## Lossless domain archives

The reader accepts the ZIP files directly. To use the raw CSVs in other software, extract each ZIP in its current folder. The verification tool supports both the distributed archives and the extracted CSVs. CSV values, row order, column labels, and missing cells are unchanged. Five domain CSVs omit their 15-line export preambles, so all released risk CSVs have headers on row 1. The reader remains compatible with original CSVs that contain preambles.
