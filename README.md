# Text Classification Annotation

## Project Overview

This project demonstrates a structured text-labeling workflow using a small set of 50 synthetic text samples. Each sample is assigned one primary label according to a documented annotation guide.

The task uses four labels: **Positive**, **Negative**, **Neutral**, and **Complaint**. The first three describe the tone or information in a message; **Complaint** identifies a message that reports a specific problem and seeks action or resolution. Because these categories can overlap, the guidelines define a clear decision order.

## Annotation Categories

| Label | When to use it |
|---|---|
| Positive | The message expresses satisfaction, praise, or a favorable experience. |
| Negative | The message expresses dissatisfaction or an unfavorable opinion without requesting a specific remedy. |
| Neutral | The message is factual or informational and has no clear positive or negative sentiment or complaint. |
| Complaint | The message reports a specific problem and asks for help, correction, investigation, replacement, refund, or another resolution. |

## Dataset

- **Records:** 50 synthetic examples
- **Format:** CSV
- **Fields:** `ID`, `Text`, `Label`
- **Label distribution:** Positive (12), Negative (13), Neutral (12), Complaint (13)

The examples are illustrative portfolio data, not customer records or production data.

## Repository Contents

| File | Purpose |
|---|---|
| `dataset.csv` | Labeled text samples |
| `annotation_guidelines.md` | Label definitions, decision order, and annotation rules |
| `evaluation_report.md` | Dataset summary and structural validation results |
| `error_analysis.md` | Ambiguous examples and label-boundary notes |

## Annotation and Quality Checks

The labeling rules define how to distinguish a negative opinion from a complaint and how to handle mixed messages. The dataset is checked for required columns, unique IDs, missing values, allowed labels, and label distribution.

These checks help identify structural problems. They do not, by themselves, establish that every label is semantically correct. This version has not been independently double-annotated, adjudicated, or measured for inter-annotator agreement.

## What This Project Demonstrates

- Applying a written labeling taxonomy
- Classifying short text samples
- Working with structured CSV data
- Documenting ambiguous label boundaries
- Performing basic dataset quality checks

## Scope and Limitations

This is a small synthetic demonstration dataset. It is intended to show the annotation workflow and documentation, not to claim production-scale annotation experience or model performance. A larger operational dataset would require independent review, disagreement resolution, and appropriate agreement measurements.
