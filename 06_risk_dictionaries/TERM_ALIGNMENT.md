# Dictionary and Data Term Comparison

This comparison uses the current published dictionary files and the actual column headers of the published domain CSVs. A dictionary entry is a nonempty line with surrounding whitespace trimmed for comparison only. Repeated entries count once when comparing sets. CSV terms are taken from the `*_count` column names after removing that suffix. Comparison operations do not rewrite files. The financial dictionary was separately updated in place using the extraction procedure recorded below; the original uploaded source files and research data were not changed.

## Risk dictionaries compared with CSV columns

| Domain | Unique published risk terms | CSV terms | Shared terms | CSV terms absent from published list | Published terms absent from CSV |
| --- | ---: | ---: | ---: | ---: | ---: |
| Environmental | 75 | 75 | 75 | 0 | 0 |
| Financial | 107 | 107 | 107 | 0 | 0 |
| Supply and demand | 96 | 96 | 96 | 0 | 0 |
| Logistics | 80 | 80 | 80 | 0 | 0 |
| System | 88 | 88 | 88 | 0 | 0 |

This verifies term-set correspondence, not how the dictionaries were generated or how every count was calculated. Political and operational dictionary files were not supplied and are not reconstructed from the data columns.

## Financial dictionary update: 67 to 107 terms

The originally supplied financial risk file contained 67 terms. The existing repository file, `03_financial/financial_risk_terms.txt`, now contains all 107 unique terms represented by the published financial CSV. It was updated by selecting the `*_count` headers, removing the `_count` suffix and retaining the CSV column order. All original 67 terms remain present. The 40 terms below were added from those headers.

The uploaded source file and all research data remain unchanged. The earlier 67-term repository version remains available in Git history. This extraction establishes correspondence with the existing data; it does not establish the original word-expansion history.

- 不利因素
- 业务发展
- 业务拓展
- 产权
- 保全
- 保全申请
- 信贷
- 借入
- 借款
- 克服
- 冻结
- 冻结资金
- 制约
- 发放贷款
- 受到限制
- 受困
- 受阻
- 受限
- 受限制
- 可供执行
- 困境
- 开拓
- 投资
- 抵押
- 抵押借款
- 拓展
- 挑战
- 控制关系
- 新设
- 有息负债
- 杠杆
- 查封
- 董事会
- 计提
- 负债
- 负债率
- 财产
- 财务
- 贷款
- 阻碍

## Seed-term overlap

A seed dictionary is not assumed to be a subset of its associated risk dictionary. The observed overlaps are:

| Domain | Unique seed terms | Seeds present in published risk dictionary | Seeds absent from published risk dictionary |
| --- | ---: | ---: | ---: |
| Environmental | 21 | 6 | 15 |
| Financial | 12 | 12 | 0 |
| Supply and demand | 42 | 42 | 0 |
| Logistics | 40 | 40 | 0 |
| System | 24 | 0 | 24 |

For the environmental and system domains, the supplied risk lists match the CSV term columns despite not containing all seed terms. Consequently, adding the seed lists to the risk lists would change the measurement dictionary. The source files are retained as separate lists; exact set differences are recorded in the [manifest](dictionary_manifest.json).
