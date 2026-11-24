# Text Classification Annotation

## Project Overview

This project demonstrates a structured text-labeling workflow using 250 synthetic text samples. Each sample is assigned one primary label according to a documented annotation guide.

The task uses four labels: **Positive**, **Negative**, **Neutral**, and **Complaint**. Positive, Negative, and Neutral describe the message's sentiment or informational content. Complaint identifies a message that reports an active problem requiring intervention. The guidelines define a decision order because these concepts can overlap.

## Annotation Categories

| Label | When to use it |
|---|---|
| Positive | The message expresses satisfaction, praise, or a favorable experience. |
| Negative | The message expresses dissatisfaction without requesting a specific remedy. |
| Neutral | The message is factual or informational, without clear sentiment or an active complaint. |
| Complaint | The message reports a specific problem that needs help, correction, investigation, replacement, refund, or another resolution. |

## Dataset

- **Records:** 250 synthetic examples
- **Format:** CSV
- **Fields:** `ID`, `Text`, `Label`
- **Label distribution:** Positive (62), Negative (63), Neutral (62), Complaint (63)

The examples are illustrative portfolio data, not customer records or production data.

## Repository Contents

| File | Purpose |
|---|---|
| `dataset.csv` | Labeled text samples |
| `annotation_guidelines.md` | Label definitions, decision order, and annotation rules |
| `evaluation_report.md` | Dataset summary, structural checks, and limitations |
| `error_analysis.md` | Ambiguous examples and label-boundary notes |
| `validate_dataset.py` | Reusable script for checking CSV structure and labels |

## Run the Validator

Run this command from the repository directory:

```bash
python3 validate_dataset.py
```

The script checks required columns, missing values, duplicate IDs, allowed labels, and label distribution. These are structural checks; they do not prove that every label is semantically correct.

## What This Project Demonstrates

- Applying a written labeling taxonomy
- Classifying short text samples
- Working with structured CSV data
- Documenting ambiguous label boundaries
- Performing basic dataset quality checks with Python

## Scope and Limitations

This is a small synthetic demonstration dataset. It is intended to show the annotation workflow and documentation, not to claim production-scale annotation experience or model performance. The dataset has not been independently double-annotated, adjudicated, or measured for inter-annotator agreement. A production workflow would require independent review, disagreement resolution, and appropriate agreement measurements.
