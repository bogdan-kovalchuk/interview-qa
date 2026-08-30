# Audit and repair DOU batch 8 discrepancy

Work in `C:/Users/bogdan/Desktop/interview-qa`.

Batch 8 report claims 20 new UK/EN pairs for Senior records 8–27, but the central
check found only 15 net-new Ukrainian files and DOU source_id files increased from
150 to 165. Audit this discrepancy before any further DOU import.

Inspect the batch report, all current cards, source Senior records 8–27, and prior
batch reports. Identify the exact five pairs that were already present, overwritten,
deleted, or otherwise failed to become net-new files. Check global ID immutability
and source Front/Back parity. If concrete damage or missing pairs is proven, repair
only those five pairs using fresh unique IDs where required, preserving the original
card content when recoverable. Do not alter unrelated cards.

Run focused checks for all Senior 8–27 coverage, exactly 20 DOU source records,
UK/EN pairing, unique IDs, source parity, HTML inline/block code or formula markup,
and forbidden characters. Do not edit registry, taxonomy, PLAN, generated outputs,
or commit/push. Write a detailed evidence report to
`temp/agent-reports/dou-batch-8-audit.md`. Stop after audit/repair; do not import
new source records.
