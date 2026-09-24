# Dictionary Source Files

Nine text files are unchanged copies of the supplied files. The financial risk dictionary was updated in place from 67 to 107 terms extracted from the financial CSV headers. Repository paths and filenames were standardised for navigation. Original source hashes, current file hashes and the financial extraction procedure are recorded in [dictionary_manifest.json](dictionary_manifest.json). The original filename column below identifies the supplied source, which remains unchanged; it does not imply that the current financial risk file is byte-identical to that 67-term source.

| Domain | Type | Repository file | Original filename |
| --- | --- | --- | --- |
| Environmental | Seed terms | [environmental_seed_terms.txt](02_environmental/environmental_seed_terms.txt) | 供应链环境风险种子词+相似0.45以上+显示100.txt |
| Environmental | Risk terms | [environmental_risk_terms.txt](02_environmental/environmental_risk_terms.txt) | 供应链环境风险词相似0.45以上显示100word2vec拓展.txt |
| Financial | Seed terms | [financial_seed_terms.txt](03_financial/financial_seed_terms.txt) | 供应链财务风险种子词+相似0.45以上+显示100.txt |
| Financial | Risk terms | [financial_risk_terms.txt](03_financial/financial_risk_terms.txt) | 供应链财务风险词相似0.45以上显示100word2vec拓展的去中性词.txt |
| Supply and demand | Seed terms | [supply_demand_seed_terms.txt](04_supply_demand/supply_demand_seed_terms.txt) | 供应链供需风险种子词补+相似0.45以上+显示100.txt |
| Supply and demand | Risk terms | [supply_demand_risk_terms.txt](04_supply_demand/supply_demand_risk_terms.txt) | 供应链供需风险词补+相似0.45以上+显示100.txt |
| Logistics | Seed terms | [logistics_seed_terms.txt](05_logistics/logistics_seed_terms.txt) | 供应链物流风险种子词补+相似0.45以上+显示100.txt |
| Logistics | Risk terms | [logistics_risk_terms.txt](05_logistics/logistics_risk_terms.txt) | 供应链物流风险词补相似0.45以上显示100word2vec拓展.txt |
| System | Seed terms | [system_seed_terms.txt](06_system/system_seed_terms.txt) | 供应链系统风险种子词+相似0.45以上+显示100.txt |
| System | Risk terms | [system_risk_terms.txt](06_system/system_risk_terms.txt) | 供应链系统风险词相似0.45以上显示100word2vec拓展.txt |

The current [financial risk dictionary](03_financial/financial_risk_terms.txt) is derived from the `*_count` column names in [financial_risk_2018_2025.csv.zip](../02_risk_disclosure_data/02_domain_data/financial_risk_2018_2025.csv.zip). See the [update record](TERM_ALIGNMENT.md) for the 40 added terms.
