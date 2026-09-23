# Domain-Level Risk Disclosure Data

Each CSV preserves the term-level inputs for one risk domain. Chinese term labels and source values remain unchanged.

| Domain | File | Header row |
| --- | --- | ---: |
| Political | [political_risk_2018_2025.csv.zip](political_risk_2018_2025.csv.zip) | 1 |
| Environmental | [environmental_risk_2018_2025.csv.zip](environmental_risk_2018_2025.csv.zip) | 1 |
| Financial | [financial_risk_2018_2025.csv.zip](financial_risk_2018_2025.csv.zip) | 1 |
| Supply and demand | [supply_demand_risk_2018_2025.csv.zip](supply_demand_risk_2018_2025.csv.zip) | 1 |
| Logistics | [logistics_risk_2018_2025.csv.zip](logistics_risk_2018_2025.csv.zip) | 1 |
| System | [system_risk_2018_2025.csv.zip](system_risk_2018_2025.csv.zip) | 1 |
| Operational | [operational_risk_2018_2025.csv.zip](operational_risk_2018_2025.csv.zip) | 1 |

[Data dictionary](../../01_research_overview/DATA_DICTIONARY.md) · [Reading guide](../../05_reading_tools/README.md)

## ZIP format

Each domain archive contains one CSV. Extract it to the same folder before analysis, or pass the ZIP path directly to the reading tool. Compression is lossless. The manifest records archive hashes, current uncompressed-file hashes, original-file hashes, and CSV data-section hashes. The documented preamble removal is a separate formatting step.
