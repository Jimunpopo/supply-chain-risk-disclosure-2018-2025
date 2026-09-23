# Research Overview

## Purpose

The research examines how different dimensions of supply chain risk disclosure are associated across adjacent years. Company annual reports provide the text from which domain-specific indicators are constructed. These indicators support a cross-lagged panel network (CLPN), with seven risk categories retained as separate variables.

The variables measure **disclosed risk-related content**. They are text-based disclosure measures rather than direct observations of realised disruption losses. Cross-lagged associations describe conditional prediction across years and do not, by themselves, establish a causal mechanism.

## Observation and coverage

| Item | Description |
| --- | --- |
| Reporting period | 2018–2025 |
| Observation in the combined panel | One company in one accounting year |
| Matching keys | Six-digit company code and accounting year |
| Combined panel | 31,321 observations from 5,018 companies |
| Political and system source files | 31,321 observations from 5,018 companies each |
| Other five source files | 27,817 observations from 4,451 companies each |
| Adjacent-year windows within the period | 2018→2019 through 2024→2025 |

The source filenames indicate industry exclusions, and the domain files have different coverage. A filename alone is not a complete, reproducible industry selection rule. The combined panel retains the union of source company–year keys. A missing domain observation remains missing rather than becoming a zero.

## Construction of domain measures

For each company, year, and risk domain:

1. Sum the domain's term-level `*_count` fields.
2. Divide this sum by the same observation's `denom`.
3. Store the resulting count and disclosure ratio in the combined panel.

The source files also retain term-level ratios and TF-IDF fields. The documented combined-panel calculation uses term counts and the original denominator.

Five source files describe their counting mode as sentence frequency. Summing counts across terms can count one sentence more than once. The domain count should therefore not be relabelled as a deduplicated count of risk sentences.

## From the base panel to the estimation sample

The base panel contains all retained company–year keys. Estimation additionally requires adjacent-year observations and the relevant complete variables.

The historical audit dated 12 September 2026 reported a reconstructed estimation sample of **21,996 company–year transitions from 3,867 companies** after matching and completeness requirements. These figures are historical audit findings. This release organises and documents the source data without rerunning that regression analysis.

## Further documentation

- [Data dictionary](DATA_DICTIONARY.md): exact panel fields and source-file structure.
- [Source file register](SOURCE_FILES.md): original and repository filenames.
- [Verification summary](../04_data_verification/README.md): current file checks and findings recorded in the earlier audit.
