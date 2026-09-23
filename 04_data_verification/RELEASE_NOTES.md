# CSV Release Formatting Update

This update standardises the downloadable CSV layout. It does not change the data or rerun the analysis.

## Files reformatted

The environmental, financial, supply and demand, logistics, and operational CSVs each originally began with 15 lines of export notes. Those lines contained an export title, generation timestamp, local Windows file path, a Stata import command, variable definitions, and separator lines. The actual column header was on line 16; the embedded Stata command referred to an older header position.

The current release copies begin directly with the original column header. Their ZIP filenames are unchanged. The preserved originals were not edited.

## Information preserved

- Column headers and every byte from the original header to the end of each CSV are unchanged.
- Values, missing cells, company codes, industry labels, years, row order, column order, decimal text, and line endings are unchanged.
- The original counting-mode description and variable formulas are retained in the [data dictionary](../01_research_overview/DATA_DICTIONARY.md).
- Original filenames and full-file SHA-256 hashes remain in the source register and manifest. The manifest separately identifies current release hashes and original data-section hashes.
- The combined panel, political and system CSVs, financial workbook, and historical audit report remain byte-identical to their originals.

## Verification

Before this update, all ten source files and all seven domain archives downloaded from GitHub matched the previous manifest. After reformatting, the five released CSVs were compared byte for byte with the corresponding original header-and-data sections. Header fields and row counts were also checked. No CSV was parsed and rewritten to perform the formatting change.

Run `python 05_reading_tools/verify_files.py` to check the distributed files against the updated manifest. The source copies are retained separately; their full-file checksums are provenance records and cannot be independently verified without obtaining those originals.

## Research scope

This is a file-format update. It does not resolve or alter the sample-coverage differences, industry-label differences, counting definitions, or historical audit findings described elsewhere in the repository. Existing Git history is retained.
