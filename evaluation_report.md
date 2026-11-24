# Dataset Evaluation and Quality Report

## 1. Scope

This report describes structural checks and documentation for the portfolio's synthetic text-classification data. It is not a semantic accuracy study or an independent annotation audit.

## 2. Main Dataset Profile

| Measure | Result |
|---|---:|
| Records | 250 |
| Unique IDs | 250 |
| Empty text fields | 0 |
| Empty labels | 0 |
| Labels outside taxonomy | 0 |
| Exact duplicate text samples (case-insensitive) | 0 |

### Label Distribution

| Label | Count | Share |
|---|---:|---:|
| Positive | 62 | 24.8% |
| Negative | 63 | 25.2% |
| Neutral | 62 | 24.8% |
| Complaint | 63 | 25.2% |
| **Total** | **250** | **100%** |

The near-balanced distribution is intentional. It must not be interpreted as the natural prevalence of these categories in customer communications.

## 3. Challenge Set

A separate file, `challenge_cases.csv`, contains 30 synthetic edge cases with an expected label and a written decision rationale. It is intended to demonstrate how the taxonomy handles mixed sentiment, implied requests, resolved issues, factual questions, and negative opinions.

The challenge set is not an independent test set: its examples and expected labels were authored as part of this portfolio exercise. It must not be used to claim external validation or unbiased model performance.

## 4. Structural Validation

Run:

```bash
python3 validate_dataset.py
```

The script checks:
- Required columns and readable CSV structure
- Non-empty IDs, text, and labels
- Duplicate IDs
- Exact duplicate text after trimming and case-folding
- Labels restricted to the approved taxonomy
- Challenge-set rationale and schema completeness
- Record totals and label distribution

A successful run establishes structural consistency only. It cannot judge whether a label is correct for the meaning of a message.

## 5. Quality Assurance Status

| QA component | Status |
|---|---|
| Written annotation taxonomy | Documented |
| Decision procedure and edge-case rules | Documented |
| Structural CSV validation | Implemented in Python |
| Synthetic challenge examples | Added |
| Independent second annotator | Not completed |
| Blind annotation comparison | Not completed |
| Adjudication log | Template provided; no real adjudication claimed |
| Cohen's kappa / inter-annotator agreement | Not measured |
| Real-world external dataset validation | Not completed |

## 6. Known Limitations and Risks

1. **Synthetic provenance:** Neither dataset establishes performance on naturally occurring customer messages.
2. **No independent review:** Current labels have not been independently double-annotated.
3. **No semantic gold standard:** Structural checks cannot confirm meaning-level correctness.
4. **Taxonomy overlap:** Sentiment and complaint intent are conceptually different dimensions. The precedence rule makes this exercise operational but may not fit every production task.
5. **Class balance:** The deliberately balanced labels do not model real-world class prevalence.
6. **Language coverage:** The examples are primarily English and do not establish multilingual annotation capability.
7. **No model evaluation:** No classifier performance or model benchmark is claimed.

## 7. Recommended Next Validation Study

1. Select a random sample from the 250 main records.
2. Hide the existing labels from a second annotator.
3. Have the second annotator apply the same guidelines independently.
4. Record both sets of labels before discussion.
5. Report raw agreement and Cohen's kappa for two annotators, with sample size and label distribution.
6. Review disagreements and record adjudicated outcomes separately.
7. Update guidelines and repeat a sample if substantial systematic ambiguity remains.

Do not calculate or publish agreement statistics from labels that were not independently produced.

## 8. Conclusion

The repository now documents a reproducible, structurally validated annotation exercise with explicit label precedence, separate challenge cases, and a defined independent-review workflow. Its strongest evidence is documentation and data handling. Its principal evidence gap remains the absence of independent human review and naturally occurring, appropriately licensed data.
## External Data Selection Decision
A possible real-world source is the [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/), which the CFPB states is freely available for anyone to use, analyze, and build on. It is not included in this release because its narrative records are complaint submissions and do not supply examples for all four labels in this project's taxonomy. Forcing those records into a four-class dataset would create a source/taxonomy mismatch. A future extension should keep a separate, clearly attributed complaint-domain dataset rather than presenting it as a balanced four-class benchmark.
