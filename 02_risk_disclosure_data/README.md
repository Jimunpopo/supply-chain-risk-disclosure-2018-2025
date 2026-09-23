# Risk Disclosure Data

This section contains the eight risk CSVs: one combined company–year panel and seven domain-level source files.

## 01 — Combined panel

[supply_chain_risk_panel_2018_2025.csv](01_combined_panel/supply_chain_risk_panel_2018_2025.csv)

The panel contains 31,321 observations, 5,018 companies, and 18 columns. It provides one count and one disclosure ratio for each of the seven domains.

## 02 — Domain-level source data

| Domain | Source file | Observations | Companies | Terms |
| --- | --- | ---: | ---: | ---: |
| Political | [political_risk_2018_2025.csv.zip](02_domain_data/political_risk_2018_2025.csv.zip) | 31,321 | 5,018 | 21 |
| Environmental | [environmental_risk_2018_2025.csv.zip](02_domain_data/environmental_risk_2018_2025.csv.zip) | 27,817 | 4,451 | 75 |
| Financial | [financial_risk_2018_2025.csv.zip](02_domain_data/financial_risk_2018_2025.csv.zip) | 27,817 | 4,451 | 107 |
| Supply and demand | [supply_demand_risk_2018_2025.csv.zip](02_domain_data/supply_demand_risk_2018_2025.csv.zip) | 27,817 | 4,451 | 96 |
| Logistics | [logistics_risk_2018_2025.csv.zip](02_domain_data/logistics_risk_2018_2025.csv.zip) | 27,817 | 4,451 | 80 |
| System | [system_risk_2018_2025.csv.zip](02_domain_data/system_risk_2018_2025.csv.zip) | 31,321 | 5,018 | 88 |
| Operational | [operational_risk_2018_2025.csv.zip](02_domain_data/operational_risk_2018_2025.csv.zip) | 27,817 | 4,451 | 39 |

## Reading notes

- Join observations by `code` and `year`.
- Keep company codes as strings to preserve leading zeros.
- Preserve the distinction between missing observations and zero counts.
- The political and system files have headers on row 1. The other five domain files have headers on row 16.
- Original Chinese term labels, introductory notes, and numerical values remain unchanged.

See the [data dictionary](../01_research_overview/DATA_DICTIONARY.md) and [reading tools](../05_reading_tools/README.md) for details.

## ZIP format

Each domain archive contains one CSV. Extract it to the same folder before analysis, or pass the ZIP path directly to the reading tool. Compression does not change any CSV content; the manifest records both archive and uncompressed-file hashes.
