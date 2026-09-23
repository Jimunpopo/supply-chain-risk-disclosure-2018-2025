# Data Verification

## Checks for this release

The following checks were completed when organising the repository on 23 September 2026:

| Check | Result |
| --- | --- |
| Source preservation | Nine data files and the historical report match their source SHA-256 hashes |
| Combined panel dimensions | 31,321 observations, 5,018 companies, 18 columns |
| CSV year coverage | All eight risk CSVs cover 2018–2025 |
| Company–year key uniqueness | No duplicate `code + year` keys within any risk CSV |
| CSV structure | Data rows have the expected number of fields |
| Header location | Row 1 for the panel, political and system files; row 16 for the other five domains |
| Reading utility | Reads all eight files and retains six-digit company codes |

These checks verify the archived files and their structure. They do not constitute a new estimation of the CLPN models.

## Findings recorded in the historical audit

The report dated **12 September 2026** compared the seven source files with the combined panel and reconstructed selected published model results. It recorded these data findings:

- Domain count sums matched the panel exactly, and ratios matched within a numerical tolerance of `1e-12`.
- Source denominators matched those in the combined panel.
- The union of source company–year keys matched the 31,321 panel keys.
- Five domains each lacked 3,504 records present in the wider political and system files. Corresponding panel cells remained missing.
- Five domains each had 586 industry-label differences from the panel, involving the same 78 companies. These are repeated differences across five files, not 2,930 distinct company–year issues.
- The reconstructed estimation sample contained 21,996 transitions from 3,867 companies.

Industry-label differences remain in the preserved source data. Analyses using industry selection or industry fixed effects should review those classifications.

## Original report and scope

[Read the original audit report — 12 September 2026, Chinese](original_report/Audit_Report_2026-09-12_Chinese.md)

The report is retained without edits. It examined the data and thesis draft available on that date. Its comments on methodological wording refer to that draft and should not be treated as a review of subsequent revisions. Some model outputs referenced in the report are outside this source-data release.

## File manifest

[file_manifest.json](file_manifest.json) records repository paths, original filenames, file sizes, and SHA-256 digests. For CSVs, it also records header positions, full field names, row and company counts, years, and duplicate-key counts.

From the repository root:

```bash
python 05_reading_tools/verify_files.py
```

The command checks ten source files and exits with a non-zero status if a file is missing or has changed. It does not modify the data.

Domain CSVs are distributed in lossless ZIP archives. The verification command checks both archive hashes and uncompressed CSV hashes. It also accepts CSVs extracted beside their archives.
