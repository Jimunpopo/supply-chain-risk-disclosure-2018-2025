# Supply Chain Risk Dictionaries

This section contains ten text files: one seed-term list and one risk-term list for each of five domains. Nine are unchanged author-supplied copies. The financial risk list has been updated in place to the 107 terms extracted from the published financial CSV column names. The dictionaries support inspection of the text measures in the [risk data catalogue](../02_risk_disclosure_data/README.md).

## Dictionary catalogue

| Domain | Seed dictionary | Risk dictionary | Unique seed terms | Unique risk terms | Relationship to published CSV |
| --- | --- | --- | ---: | ---: | --- |
| Political | Not supplied | Not supplied | — | — | Dictionary files are not included in this release |
| Environmental | [Seed terms](02_environmental/environmental_seed_terms.txt) | [Risk terms](02_environmental/environmental_risk_terms.txt) | 21 | 75 | Matches CSV term set |
| Financial | [Seed terms](03_financial/financial_seed_terms.txt) | [Risk terms](03_financial/financial_risk_terms.txt) | 12 | 107 | Matches CSV term set; extracted from CSV headers |
| Supply and demand | [Seed terms](04_supply_demand/supply_demand_seed_terms.txt) | [Risk terms](04_supply_demand/supply_demand_risk_terms.txt) | 42 | 96 | Matches CSV term set |
| Logistics | [Seed terms](05_logistics/logistics_seed_terms.txt) | [Risk terms](05_logistics/logistics_risk_terms.txt) | 40 | 80 | Matches CSV term set |
| System | [Seed terms](06_system/system_seed_terms.txt) | [Risk terms](06_system/system_risk_terms.txt) | 24 | 88 | Matches CSV term set |
| Operational | Not supplied | Not supplied | — | — | Dictionary files are not included in this release |

Counts above ignore blank lines and trim surrounding whitespace for comparison only. The nine unchanged files preserve all original bytes, including repeated entries, blank lines, spacing and term order. The financial risk file lists the 107 CSV terms in column order, one term per line. For example, the logistics risk file contains 83 nonempty entries representing 80 unique terms.

## Seed terms and risk terms

Files identified as seed terms and risk terms are kept separately. Inclusion of seed terms in a published risk dictionary differs by domain; these files should not be automatically combined. Their contents and relationships are documented in the [term comparison](TERM_ALIGNMENT.md).

The original filenames record a similarity threshold of 0.45 and a display setting of 100; several also identify Word2Vec expansion. These are filename annotations. The supplied text files do not contain the model, training corpus, similarity scores or generation code, so those settings cannot be independently verified from the lists alone. The display setting is not the number of terms in each delivered file.

## Correspondence with the released data

All five published risk dictionaries now match the unique term names in their respective CSVs. The financial risk file was expanded from the supplied 67-term list to all 107 terms present in the financial CSV. The same repository filename is used. The 40 added terms come directly from the CSV headers; no terms were invented.

This update documents the term set represented in the existing financial data. It does not reconstruct the original Word2Vec generation process or recalculate any risk values. The uploaded 67-term source file remains unchanged outside the repository, and its earlier repository version remains in Git history. See the [comparison and update record](TERM_ALIGNMENT.md).

## Source files and integrity

The [source register](SOURCE_FILES.md) maps clear repository filenames to the original filenames. The [dictionary manifest](dictionary_manifest.json) records SHA-256 hashes, file sizes and comparison counts for all ten files. Nine repository text files are byte-identical to their supplied sources. For the financial risk file, the manifest separately records the original 67-term source hash, the current 107-term file hash, and the CSV extraction procedure. The existing data-file manifest and its ten-file verification command remain separate.
