# Dataset Evaluation Report

## Dataset Summary

| Measure | Result |
|---|---:|
| Total records | 250 |
| Unique IDs | 250 |
| Missing text values | 0 |
| Missing labels | 0 |
| Labels outside the approved taxonomy | 0 |
| Exact duplicate text samples | 0 |

## Label Distribution

| Primary label | Count | Share |
|---|---:|---:|
| Positive | 62 | 24.8% |
| Negative | 63 | 25.2% |
| Neutral | 62 | 24.8% |
| Complaint | 63 | 25.2% |
| **Total** | **250** | **100%** |

The four classes are nearly balanced. This is a deliberately constructed portfolio dataset; the distribution is not intended to represent the frequency of these labels in real customer messages.

## Validation

The dataset was checked for:
- Required columns: `ID`, `Text`, and `Label`
- Unique, non-empty record IDs
- Non-empty text and label fields
- Labels restricted to the four categories in the annotation guide
- Exact duplicate text samples
- Record and label counts

Run the included validation script from the repository root:

```bash
python3 validate_dataset.py
```

The script checks structural integrity and reports the label distribution. It does not determine whether every label is semantically correct.

## Dataset Composition

The 250 examples cover common message contexts such as:
- Product quality and usability
- Customer support and service experiences
- Orders, delivery, returns, and refunds
- Payments, subscriptions, and account access
- Scheduling, bookings, and general information
- Software, devices, websites, and digital services

## Annotation Quality and Limitations

The examples are synthetic and were prepared for demonstration. The dataset has not undergone independent double annotation, formal adjudication, or inter-annotator agreement measurement. No model training or model-performance evaluation is claimed.

A stronger production workflow would include:
1. Independent annotation by at least two annotators on an agreed sample.
2. Disagreement review and documented adjudication.
3. Calculation of an appropriate agreement statistic, such as Cohen's kappa for two annotators.
4. Guideline revision and re-annotation where recurring ambiguity is found.
5. A versioned audit trail for dataset and guideline changes.

## Conclusion

The expanded dataset demonstrates a larger, nearly balanced, documented four-way labeling workflow with basic structural quality checks. Its synthetic nature means it remains a portfolio exercise, not a production benchmark or evidence of real-world generalization.
