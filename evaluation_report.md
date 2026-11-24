# Dataset Evaluation Report

## Dataset Summary

| Measure | Result |
|---|---:|
| Total records | 50 |
| Unique IDs | 50 |
| Missing text values | 0 |
| Missing labels | 0 |
| Labels outside the approved taxonomy | 0 |

## Label Distribution

| Primary label | Count |
|---|---:|
| Positive | 12 |
| Negative | 13 |
| Neutral | 12 |
| Complaint | 13 |
| **Total** | **50** |

The categories are nearly balanced in this deliberately constructed sample. This distribution should not be interpreted as representative of real customer messages.

## Validation

The dataset has been checked for:
- Required columns: `ID`, `Text`, and `Label`
- Unique record IDs
- Non-empty text and label fields
- Labels restricted to the four categories in the annotation guide
- Record and label counts

Run the included validation script from the repository root:

```bash
python3 validate_dataset.py
```

The script checks structural integrity and reports the label distribution. It does not determine whether a label is semantically correct.

## Annotation Quality and Limitations

The examples are synthetic and were prepared for demonstration. The dataset has not undergone independent double annotation, formal adjudication, or inter-annotator agreement measurement. No model training or model-performance evaluation is claimed.

A stronger production workflow would include:
1. Independent annotation by at least two annotators on an agreed sample.
2. Disagreement review and documented adjudication.
3. Calculation of an appropriate agreement statistic, such as Cohen's kappa for two annotators.
4. Guideline revision and re-annotation where recurring ambiguity is found.
5. A versioned audit trail for dataset and guideline changes.

## Conclusion

The current dataset demonstrates a documented four-way labeling workflow and basic structural quality checks. Its size and synthetic nature make it suitable as a portfolio exercise, not as a production benchmark or evidence of real-world generalization.
