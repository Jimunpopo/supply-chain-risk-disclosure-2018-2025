# Dictionary and Data Term Comparison

This comparison uses the supplied text files and the actual column headers of the published domain CSVs. A dictionary entry is a nonempty line with surrounding whitespace trimmed for comparison only. Repeated entries count once when comparing sets. CSV terms are taken from the `*_count` column names after removing that suffix. These operations do not rewrite the supplied files or the data.

## Risk dictionaries compared with CSV columns

| Domain | Unique supplied risk terms | CSV terms | Shared terms | CSV terms absent from supplied list | Supplied terms absent from CSV |
| --- | ---: | ---: | ---: | ---: | ---: |
| Environmental | 75 | 75 | 75 | 0 | 0 |
| Financial | 67 | 107 | 67 | 40 | 0 |
| Supply and demand | 96 | 96 | 96 | 0 | 0 |
| Logistics | 80 | 80 | 80 | 0 | 0 |
| System | 88 | 88 | 88 | 0 | 0 |

This verifies term-set correspondence, not how the dictionaries were generated or how every count was calculated. Political and operational dictionary files were not supplied and are not reconstructed from the data columns.

## Financial dictionary version

The supplied financial risk file is a 67-term subset of the 107-term CSV dictionary. Its filename describes removal of neutral terms, but the files alone do not establish when that version was produced or used. The following 40 terms occur in the released financial CSV and are absent from the supplied financial risk list:

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

| Domain | Unique seed terms | Seeds present in supplied risk dictionary | Seeds absent from supplied risk dictionary |
| --- | ---: | ---: | ---: |
| Environmental | 21 | 6 | 15 |
| Financial | 12 | 10 | 2 |
| Supply and demand | 42 | 42 | 0 |
| Logistics | 40 | 40 | 0 |
| System | 24 | 0 | 24 |

For the environmental and system domains, the supplied risk lists match the CSV term columns despite not containing all seed terms. Consequently, adding the seed lists to the risk lists would change the measurement dictionary. The source files are retained as separate lists; exact set differences are recorded in the [manifest](dictionary_manifest.json).
