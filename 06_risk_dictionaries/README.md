# Supply Chain Risk Dictionaries

This section contains ten author-supplied text files: one seed-term list and one risk-term list for each of five domains. The dictionaries support inspection of the text measures in the [risk data catalogue](../02_risk_disclosure_data/README.md).

## Dictionary catalogue

| Domain | Seed dictionary | Risk dictionary | Unique seed terms | Unique risk terms | Relationship to published CSV |
| --- | --- | --- | ---: | ---: | --- |
| Political | Not supplied | Not supplied | — | — | Dictionary files are not included in this release |
| Environmental | [Seed terms](02_environmental/environmental_seed_terms.txt) | [Risk terms](02_environmental/environmental_risk_terms.txt) | 21 | 75 | Matches CSV term set |
| Financial | [Seed terms](03_financial/financial_seed_terms.txt) | [Risk terms](03_financial/financial_risk_terms.txt) | 12 | 67 | 67 of 107 CSV terms; see comparison |
| Supply and demand | [Seed terms](04_supply_demand/supply_demand_seed_terms.txt) | [Risk terms](04_supply_demand/supply_demand_risk_terms.txt) | 42 | 96 | Matches CSV term set |
| Logistics | [Seed terms](05_logistics/logistics_seed_terms.txt) | [Risk terms](05_logistics/logistics_risk_terms.txt) | 40 | 80 | Matches CSV term set |
| System | [Seed terms](06_system/system_seed_terms.txt) | [Risk terms](06_system/system_risk_terms.txt) | 24 | 88 | Matches CSV term set |
| Operational | Not supplied | Not supplied | — | — | Dictionary files are not included in this release |

Counts above ignore blank lines and trim surrounding whitespace for comparison only. The downloadable files preserve all original bytes, including repeated entries, blank lines, spacing and term order. For example, the logistics risk file contains 83 nonempty entries representing 80 unique terms.

## Seed terms and risk terms

Files identified as seed terms and risk terms are kept separately. Inclusion of seed terms in a supplied risk dictionary differs by domain; these files should not be automatically combined. Their contents and relationships are documented in the [term comparison](TERM_ALIGNMENT.md).

The original filenames record a similarity threshold of 0.45 and a display setting of 100; several also identify Word2Vec expansion. These are filename annotations. The supplied text files do not contain the model, training corpus, similarity scores or generation code, so those settings cannot be independently verified from the lists alone. The display setting is not the number of terms in each delivered file.

## Correspondence with the released data

The environmental, supply and demand, logistics and system risk dictionaries match the unique term names in their respective published CSVs. The supplied financial risk dictionary contains 67 unique terms, all present among the 107 financial CSV terms. Forty CSV terms are absent from this supplied list. Its original filename identifies it as a version with neutral terms removed; the generation history and intended relationship to the released data have not been established.

These supplied lists are published without replacing or recalculating any existing risk data. The financial list should not be described as the complete 107-term dictionary used by the current CSV. See the [comparison and exact differences](TERM_ALIGNMENT.md).

## Source files and integrity

The [source register](SOURCE_FILES.md) maps clear repository filenames to the original filenames. The [dictionary manifest](dictionary_manifest.json) records SHA-256 hashes, file sizes and comparison counts for all ten files. Each repository text file is byte-identical to its supplied source. The existing data-file manifest and its ten-file verification command remain separate.
