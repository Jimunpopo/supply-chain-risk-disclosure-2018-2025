# Dictionary Files

Nine text files are unchanged copies of the supplied files. The financial risk dictionary was updated in place from 67 to 107 terms extracted from the financial CSV headers. Repository paths and filenames were standardised for navigation. Original source hashes, current file hashes and the financial extraction procedure are recorded in [dictionary_manifest.json](dictionary_manifest.json).

| Domain | Type | Repository file |
| --- | --- | --- |
| Environmental | Seed terms | [environmental_seed_terms.txt](02_environmental/environmental_seed_terms.txt) |
| Environmental | Risk terms | [environmental_risk_terms.txt](02_environmental/environmental_risk_terms.txt) |
| Financial | Seed terms | [financial_seed_terms.txt](03_financial/financial_seed_terms.txt) |
| Financial | Risk terms | [financial_risk_terms.txt](03_financial/financial_risk_terms.txt) |
| Supply and demand | Seed terms | [supply_demand_seed_terms.txt](04_supply_demand/supply_demand_seed_terms.txt) |
| Supply and demand | Risk terms | [supply_demand_risk_terms.txt](04_supply_demand/supply_demand_risk_terms.txt) |
| Logistics | Seed terms | [logistics_seed_terms.txt](05_logistics/logistics_seed_terms.txt) |
| Logistics | Risk terms | [logistics_risk_terms.txt](05_logistics/logistics_risk_terms.txt) |
| System | Seed terms | [system_seed_terms.txt](06_system/system_seed_terms.txt) |
| System | Risk terms | [system_risk_terms.txt](06_system/system_risk_terms.txt) |

The current [financial risk dictionary](03_financial/financial_risk_terms.txt) is derived from the `*_count` column names in [financial_risk_2018_2025.csv.zip](../02_risk_disclosure_data/02_domain_data/financial_risk_2018_2025.csv.zip). See the [update record](TERM_ALIGNMENT.md) for the 40 added terms.
