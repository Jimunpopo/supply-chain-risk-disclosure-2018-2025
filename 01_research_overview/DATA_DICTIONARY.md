# Data Dictionary

## Common identifiers

| Field | Meaning | Reading guidance |
| --- | --- | --- |
| `code` | Six-digit company code | Keep as text to retain leading zeros |
| `industry` | Industry label in the source file | Labels may differ across source files |
| `year` | Accounting year, 2018–2025 | Match jointly with company code |
| `denom` | Original text denominator used in the indicator | Preserve the source definition and value |

## Combined panel variables

The combined panel has four identifier/denominator fields and the following fourteen domain fields.

| Domain | Aggregated count | Disclosure ratio |
| --- | --- | --- |
| Political | `political_count_sum` | `political_risk_ratio` |
| Environmental | `environmental_count_sum` | `environmental_risk_ratio` |
| Financial | `financial_count_sum` | `financial_risk_ratio` |
| Supply and demand | `supply_demand_count_sum` | `supply_demand_risk_ratio` |
| Logistics | `logistic_count_sum` | `logistic_risk_ratio` |
| System | `system_count_sum` | `system_risk_ratio` |
| Operational | `operational_count_sum` | `operational_risk_ratio` |

For each domain, `count_sum` is the sum of the term-level `*_count` fields, and `risk_ratio` is this sum divided by `denom`. Each domain retains its own pair of fields.

The stored field prefix for logistics is `logistic`, and the stored field prefix for system risk is `system`. These field names are unchanged.

## Domain source files

Each domain CSV contains the four common fields followed by term-level `*_count`, `*_ratio`, and `*_tfidf` fields. The original Chinese term labels are preserved. All field names are listed in the [file manifest](../04_data_verification/file_manifest.json).

| Dataset | Header row | Data rows | Companies | Columns | Terms |
| --- | ---: | ---: | ---: | ---: | ---: |
| Combined panel | 1 | 31,321 | 5,018 | 18 | — |
| Political | 1 | 31,321 | 5,018 | 67 | 21 |
| Environmental | 16 | 27,817 | 4,451 | 229 | 75 |
| Financial | 16 | 27,817 | 4,451 | 325 | 107 |
| Supply and demand | 16 | 27,817 | 4,451 | 292 | 96 |
| Logistics | 16 | 27,817 | 4,451 | 244 | 80 |
| System | 1 | 31,321 | 5,018 | 268 | 88 |
| Operational | 16 | 27,817 | 4,451 | 121 | 39 |

Header positions are one-based and were checked against the current file contents. Five source files contain introductory notes before the header on row 16. Some embedded import instructions use an older header position; use the actual header or the supplied reader.

## Missing values and coverage

The political and system files cover a wider set of company–year keys than the other five domains. The panel retains the union of those keys. Missing domain values indicate absent source observations and should not automatically be converted to zero.

A zero count records no occurrences under the original counting procedure for an available observation. The count is a disclosure measure, not proof that a company faced no underlying risk.

## Financial control variables

See the [financial workbook guide](../03_financial_control_data/README.md) for field definitions, descriptive rows, and matching keys. Controls remain separate from the combined risk panel.
