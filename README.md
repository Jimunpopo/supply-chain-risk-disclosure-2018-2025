# Supply Chain Risk Disclosure in Chinese Listed Firms

## Research Data and Supporting Documentation, 2018–2025

This repository contains the data used to study seven dimensions of supply chain risk disclosure: **political, environmental, financial, supply and demand, logistics, system, and operational risk**. It is organised for dissertation review, with separate sections for the combined panel, domain-level source data, financial controls, and verification records.

The combined panel contains **31,321 firm–year observations from 5,018 firms**. Each observation identifies a company and an accounting year. Coverage differs across domains, as documented in the data catalogue.

## Start here

| Review purpose | Starting point |
| --- | --- |
| Understand the research data and measurement approach | [Research overview](01_research_overview/README.md) |
| Check variable definitions and field names | [Data dictionary](01_research_overview/DATA_DICTIONARY.md) |
| Inspect the seven risk measures together | [Combined risk panel](02_risk_disclosure_data/01_combined_panel/supply_chain_risk_panel_2018_2025.csv) |
| Trace a risk measure to its term-level inputs | [Risk data catalogue](02_risk_disclosure_data/README.md) |
| Review the separate financial control variables | [Financial control data](03_financial_control_data/README.md) |
| Check file integrity and historical audit evidence | [Data verification](04_data_verification/README.md) |

## Repository structure

| Folder | Contents |
| --- | --- |
| `01_research_overview` | Research context, data dictionary, and original filename mapping |
| `02_risk_disclosure_data` | One combined panel and seven domain-level CSV files |
| `03_financial_control_data` | Original financial workbook and field guide |
| `04_data_verification` | Verification summary, file manifest, and original dated audit report |
| `05_reading_tools` | Python tools for reading source CSVs and checking file integrity |

## How the files relate

The domain files contain term-level counts and other text measures. The combined panel joins the domain measures on **company code (`code`) and accounting year (`year`)**. It retains a separate count and disclosure ratio for each domain, producing 18 columns in total.

The seven domains remain separate variables in the cross-lagged panel network (CLPN). The combined panel does not contain a single score obtained by adding the seven risk ratios. Financial controls are supplied in a separate workbook and require their own company–year match.

## Reading and verification

Source CSVs retain their original contents, including Chinese term labels and, in five files, introductory notes. The reading tool locates the actual header and preserves leading zeros in company codes.

Run these commands from the repository root:

```bash
python 05_reading_tools/read_risk_csv.py 02_risk_disclosure_data/01_combined_panel/supply_chain_risk_panel_2018_2025.csv --rows 2
python 05_reading_tools/verify_files.py
```

The tools use the Python standard library. See the [reading guide](05_reading_tools/README.md) for further details.

## Scope of this release

This release contains **eight risk CSVs, one financial workbook, supporting documentation, and two reading and verification tools**. The seven domain CSVs are supplied in lossless ZIP archives to meet browser upload limits. After extraction, all nine data files preserve the source bytes. English filenames support navigation, with original filenames recorded in the [source file register](01_research_overview/SOURCE_FILES.md).

The historical audit is dated **12 September 2026**. Its comments on thesis wording refer to the version reviewed on that date. This release provides source data and the audit record; it does not include the full regression code or all model output files mentioned in that report.
