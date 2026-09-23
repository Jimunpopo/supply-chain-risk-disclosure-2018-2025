# Financial Control Variables

[Download the original financial workbook](financial_control_variables.xlsx)

This workbook supplies financial variables for company–year matching. It is separate from the financial **risk disclosure** file, which contains text-derived measures. No financial control columns are already incorporated in the combined risk panel.

## Workbook layout

| Position in `sheet1` | Contents |
| --- | --- |
| Row 1 | Field codes |
| Row 2 | Original Chinese field labels |
| Row 3 | Units |
| Row 4 onwards | Data records |

Match `Stkcd` to the risk panel's `code`, preserving a six-digit company identifier. Match the accounting year in `accper` to `year`.

## Field guide

| Field | English description |
| --- | --- |
| `Stkcd` | Company code |
| `accper` | Accounting year |
| `stknme` | Company short name |
| `F040201B` | Accounts receivable turnover, definition A |
| `F040501B` | Inventory turnover, definition A |
| `A002108000` | Accounts payable |
| `Outcap1` | Cash flow to capital expenditure ratio |
| `F062401B` | Free cash flow to the firm |
| `F060301B` | Operating cash flow relative to operating revenue |
| `F061701B` | Total cash recovery ratio |
| `F051201B` | Return on invested capital (ROIC) |
| `Outcap2` | Capital expenditure ratio |
| `F010101A` | Current ratio |
| `A002101000` | Short-term borrowing |
| `A001111000` | Net accounts receivable |
| `A001000000a` | Total assets |
| `C001000000` | Net cash flow from operating activities |
| `C002000000` | Net cash flow from investing activities |

The descriptions translate workbook labels. Original labels and units remain in the workbook. Ratios with provider-specific definitions should retain their original field codes when used or reported.

## Use in analysis

The workbook contains raw source fields. Transformations such as taking logarithms, scaling by total assets, or winsorisation belong to the analysis specification and are not applied to this archived workbook.

The [historical audit](../04_data_verification/README.md) records the transformations used in the September 2026 reconstruction. In particular, `F051201B` is ROIC and should not be relabelled as return on assets.
